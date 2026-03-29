"""
PQN Swarm Hub - Detector Bridge

Thin wrapper calling a detector runner and parsing detector artifacts into
structured results for submission.

In the monorepo, the default runner is `pqn_alignment.run_detector()`.
In standalone mode, a runner can be injected explicitly for tests or for an
external detector package.
"""

import csv
import importlib
import json
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

from .contracts import PQNWorkUnit


DetectorRunner = Callable[[Dict[str, Any]], Tuple[str, str]]


class DetectorBridge:
    """
    Bridge between pqn_swarm_hub work units and pqn_alignment detector.

    Calls run_detector(config) and parses output artifacts (CSV + JSONL)
    into a structured result dict suitable for SubmissionSink.
    """

    def __init__(
        self,
        runner: Optional[DetectorRunner] = None,
        detector_module_path: str = "modules.ai_intelligence.pqn_alignment",
        detector_attr: str = "run_detector",
    ) -> None:
        self._runner = runner
        self._detector_module_path = detector_module_path
        self._detector_attr = detector_attr

    def _resolve_runner(self) -> DetectorRunner:
        if self._runner is not None:
            return self._runner

        module = importlib.import_module(self._detector_module_path)
        runner = getattr(module, self._detector_attr, None)
        if runner is None:
            raise ImportError(
                f"Detector runner '{self._detector_attr}' not found in "
                f"'{self._detector_module_path}'"
            )
        return runner

    def run(self, work_unit: PQNWorkUnit) -> Dict[str, Any]:
        """
        Execute detector for a work unit and parse results.

        Args:
            work_unit: PQNWorkUnit with config dict containing detector params

        Returns:
            Dict with:
                - events_path: str path to JSONL events
                - metrics_csv: str path to CSV metrics
                - metrics: dict with coherence, pqn_rate, paradox_rate, resonance_hz
                - steps: int total steps executed
                - raw_config: original config passed to detector
        """
        # Build detector config from work unit
        config = dict(work_unit.config)  # shallow copy

        # Run detector - returns (events_path, metrics_csv)
        run_detector = self._resolve_runner()
        events_path, metrics_csv = run_detector(config)

        # Parse artifacts to extract metrics
        metrics = self._parse_metrics(events_path, metrics_csv, config)

        return {
            "events_path": events_path,
            "metrics_csv": metrics_csv,
            "metrics": metrics,
            "steps": config.get("steps", 1200),
            "raw_config": config,
        }

    def _parse_metrics(
        self,
        events_path: str,
        metrics_csv: str,
        config: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Parse detector artifacts to extract metrics for verification.

        Reads:
        - CSV for mean coherence (C column)
        - JSONL for event counts (PQN_DETECTED, PARADOX_RISK, RESONANCE_HIT)

        Returns:
            Dict with coherence, pqn_rate, paradox_rate, resonance_hz
        """
        steps = config.get("steps", 1200)

        # Parse CSV for coherence
        coherence_values: List[float] = []
        if Path(metrics_csv).exists():
            coherence_values = self._parse_coherence_from_csv(metrics_csv)

        # Parse events for rates
        event_counts, resonance_freqs = self._parse_events(events_path)

        # Compute metrics
        mean_coherence = (
            sum(coherence_values) / len(coherence_values)
            if coherence_values
            else 0.0
        )

        pqn_count = event_counts.get("PQN_DETECTED", 0)
        paradox_count = event_counts.get("PARADOX_RISK", 0)

        pqn_rate = pqn_count / steps if steps > 0 else 0.0
        paradox_rate = paradox_count / steps if steps > 0 else 0.0

        # Modal resonance frequency (most common hit)
        resonance_hz = self._modal_frequency(resonance_freqs)

        return {
            "coherence": round(mean_coherence, 6),
            "pqn_rate": round(pqn_rate, 6),
            "paradox_rate": round(paradox_rate, 6),
            "resonance_hz": round(resonance_hz, 3) if resonance_hz else None,
            "pqn_count": pqn_count,
            "paradox_count": paradox_count,
            "resonance_hit_count": len(resonance_freqs),
            "sample_count": len(coherence_values),
        }

    def _parse_coherence_from_csv(self, metrics_csv: str) -> List[float]:
        """Parse C (coherence) column from detector CSV."""
        values = []
        try:
            with open(metrics_csv, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    c_str = row.get("C", "")
                    if c_str:
                        try:
                            values.append(float(c_str))
                        except ValueError:
                            pass
        except (OSError, IOError):
            pass
        return values

    def _parse_events(self, events_path: str) -> tuple:
        """
        Parse JSONL events for flag counts and resonance frequencies.

        Returns:
            (event_counts dict, resonance_freqs list)
        """
        event_counts: Dict[str, int] = {}
        resonance_freqs: List[float] = []

        try:
            with open(events_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        event = json.loads(line)
                        flags = event.get("flags", []) or []
                        for flag in flags:
                            event_counts[flag] = event_counts.get(flag, 0) + 1
                        # Extract resonance frequency if present
                        if "RESONANCE_HIT" in flags:
                            freq = event.get("reso_freq")
                            if freq is not None:
                                resonance_freqs.append(float(freq))
                    except (json.JSONDecodeError, TypeError, ValueError):
                        pass
        except (OSError, IOError):
            pass

        return event_counts, resonance_freqs

    def _modal_frequency(self, freqs: List[float]) -> Optional[float]:
        """Return modal (most common) frequency, binned to 0.1 Hz."""
        if not freqs:
            return None
        # Bin to 0.1 Hz resolution
        bins: Dict[float, int] = {}
        for f in freqs:
            binned = round(f, 1)
            bins[binned] = bins.get(binned, 0) + 1
        # Return bin with highest count
        modal = max(bins, key=lambda k: bins[k])
        return modal

