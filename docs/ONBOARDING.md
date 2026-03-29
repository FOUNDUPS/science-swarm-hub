# ONBOARDING — Science Swarm Hub FoundUp

> Guide for external researchers and contributors joining the Science Swarm.

---

## What is the Science Swarm Hub?

The Science Swarm Hub is a FoundUp that coordinates distributed scientific computation. Researchers contribute by running bounded computational tasks (PQN work units), submitting results (rESP submissions), and earning contribution scores (ROC) for verified work.

---

## Current Status

The Science Swarm Hub is in **Phase 1 (Internal Proto)**. External contributor access is not yet open, but this document describes the intended workflow so you can prepare.

The participant gate will enforce entry policy once external access opens.

---

## How It Works

### 1. Discover Work Units

Browse available PQN work units through the registry. Each work unit defines a specific computational task with a detector configuration.

```python
# List available work units
work_units = registry.list_work_units(status_filter="pending", limit=10)
```

### 2. Run the Computation

Execute the work unit using the detector bridge or your own compatible implementation. The configuration specifies exact parameters for reproducibility.

```python
# Run via detector bridge
bridge = DetectorBridge()
result = bridge.run(work_unit)
```

### 3. Submit Results

Submit your results through the rESP submission sink. Include metrics and artifact references.

```python
# Submit results
submission = sink.submit_from_detector(
    work_unit_id=work_unit.work_unit_id,
    bridge_result=result,
    submitter_id="your_id"
)
```

### 4. Verification

Your submission enters the verification queue. The system checks result validity against defined thresholds. Future: triple-match verification where multiple independent results must agree.

### 5. Contribution Scoring

Verified submissions earn a ROC (Recursive Output Contribution) score. Your score reflects the quality and consistency of your contributions.

---

## What You Need

### Technical Requirements

- Python 3.10+
- Access to the Science Swarm Hub API (when available)
- Ability to run detector computations locally or via provided infrastructure

### Knowledge Requirements

- Understanding of the PQN work unit format (see INTERFACE.md)
- Familiarity with the rESP submission schema
- Understanding of verification criteria

---

## Getting Started (When External Access Opens)

1. **Register** through the participant gate
2. **Read** INTERFACE.md for contract definitions
3. **Browse** available work units
4. **Run** a computation
5. **Submit** results
6. **Track** your contributions and scores

---

## Key Documents

| Document | Purpose |
|---|---|
| [README.md](../README.md) | Overview and current status |
| [INTERFACE.md](../INTERFACE.md) | Contract definitions and API surface |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | System design and data flow |
| [EXFOLIATION_CHECKLIST.md](./EXFOLIATION_CHECKLIST.md) | Spin-out readiness criteria |

---

## Questions?

This is a pre-exfoliation repo. For now, the active development happens in [Foundups-Agent](https://github.com/FOUNDUPS/Foundups-Agent). Issues and discussions will be enabled here as external access opens.
