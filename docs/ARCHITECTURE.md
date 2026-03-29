# ARCHITECTURE — PQN Swarm Hub

> System design and data flow documentation.

---

## Overview

The PQN Swarm Hub is a FoundUp that coordinates distributed scientific computation. It manages the full lifecycle from task definition through result verification to contribution scoring.

The system is currently built as an integrated module inside Foundups-Agent at `modules/foundups/pqn_swarm_hub/`. At Proto (Phase 3), it will exfoliate into this standalone repo.

---

## Core Components

### 1. Work Unit Registry (`registry.py`)

The registry manages PQN work units — bounded, reproducible computational tasks. Each work unit contains a detector configuration (steps, dt, seed) that defines exactly what computation to perform.

Work units follow a state machine: `pending` -> `in_progress` -> `completed` (or `cancelled`).

The registry is the entry point for all work. Nothing happens in the system without a registered work unit.

### 2. rESP Submission Sink (`submission_sink.py`)

The submission sink accepts structured result submissions tied to work units. Each submission includes metrics (coherence, pqn_rate, paradox_rate, resonance_hz) and artifact references.

Submissions can arrive via two paths:
- Direct submission: external caller provides metrics and artifacts manually
- Detector bridge: automated path where DetectorBridge runs the detector and formats results

All submissions are tagged with source identity and linked to their parent work unit.

### 3. Detector Bridge (`detector_bridge.py`)

The bridge connects the PQN Swarm Hub to the pqn_alignment detector engine. It translates work unit configurations into detector calls and parses the output into submission-ready format.

This is an adapter — it isolates the hub from detector implementation details.

### 4. Verification Engine (`verification.py`)

Verification determines whether a submission is accepted or rejected. Current implementation uses a phi-floor threshold (0.618) on coherence metrics, with manual override capability.

Future: triple-match verification where three independent results must agree before acceptance.

### 5. Contribution Scoring (`contribution.py`)

Once a submission is verified, contribution scoring calculates a ROC (Recursive Output Contribution) score. The score considers the work performed and produces a durable JSON artifact.

Hooks exist for complexity weighting and consistency scoring (not yet active).

### 6. FAM Adapter (`fam_adapter.py` — planned)

The adapter will emit contribution events to the FAMDaemon for downstream processing (ledger, token hooks, distribution). This is a one-way emit — no direct mutation of FAM state.

---

## Data Flow

```
1. REGISTRATION
   Creator -> registry.register_work_unit(description, config)
   Output: PQNWorkUnit (status: pending)

2. EXECUTION
   DetectorBridge.run(work_unit)
   - Calls pqn_alignment.run_detector(config)
   - Parses events and metrics from output
   Output: bridge_result dict

3. SUBMISSION
   sink.submit_from_detector(work_unit_id, bridge_result, submitter_id)
   - Validates schema
   - Tags source
   - Links to work unit
   Output: rESPSubmission (status: pending_verification)

4. VERIFICATION
   verify_submission(submission_id, decision, verifier_id, rationale)
   - Checks coherence against phi-floor (0.618)
   - Records accept/reject with rationale
   Output: VerificationDecision

5. CONTRIBUTION
   record_contribution(work_unit_id, submission_id, decision_id, contributor_id, score)
   - Calculates ROC score
   - Writes durable JSON artifact
   Output: ContributionRecord

6. PUBLICATION (planned)
   fam_adapter.emit_contribution_event(ContributionRecord)
   - One-way emit to FAMDaemon
   - No direct core mutation
```

---

## Boundary Rules

The hub operates under strict boundary discipline:

**Adapter boundary:** All communication with FAMDaemon goes through a dedicated adapter. No direct mutation of the FAM event store or core control-plane modules.

**Contract discipline:** All external-facing data structures live in `contracts.py`. No scattered models.

**Interface discipline:** All callable surfaces are documented in `INTERFACE.md`. No silent API growth.

**Detector isolation:** The hub does not call the detector directly. It goes through DetectorBridge, which handles translation and error mapping.

---

## Persistence

Phase 0 (current): In-memory storage only. State does not survive restart.

Phase 1 (next): SQLite persistence for all contracts. State survives restart.

Phase 2+: Pluggable storage backend for standalone deployment.

---

## Exfoliation Design

The module is structured for clean spin-out:

- No hidden dependencies on other Foundups-Agent internals
- All shared touchpoints documented in INTERFACE.md
- Adapter stubs remain viable after spin-out
- DetectorBridge can be reconfigured to call detector via API instead of import
