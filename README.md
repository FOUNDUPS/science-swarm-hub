# PQN Swarm Hub — Science Swarm FoundUp

> **Status:** Integrated Module (Pre-Exfoliation)
> **Owner:** 0102
> **Domain:** `modules/foundups/` (WSP 3 functional distribution)
> **Active Build:** [`Foundups-Agent/modules/foundups/pqn_swarm_hub/`](https://github.com/FOUNDUPS/Foundups-Agent/tree/main/modules/foundups/pqn_swarm_hub)

---

## What This Repo Is

This is the **external-facing reference repo** for the PQN Swarm Hub FoundUp.

The active build lives inside [Foundups-Agent](https://github.com/FOUNDUPS/Foundups-Agent) as an integrated module. This repo exists to:

- Document the public interface and contracts for future external contributors
- Track the exfoliation checklist (when this repo becomes the primary codebase)
- Provide onboarding guidance for researchers joining the swarm
- Stabilize the architecture documentation independent of the build

**This repo will become the primary repo at Proto (Phase 3) spin-out.**

---

## System Purpose

The PQN Swarm Hub coordinates distributed scientific computation through three core mechanisms:

- **PQN (Provable Quantum Numeric):** Bounded work units that define reproducible computational tasks
- **rESP (recursive Evidence Submission Protocol):** Structured intake for result submissions with schema validation and source tagging
- **ROC (Recursive Output Contribution):** Contribution measurement that scores verified work for reward eligibility

---

## Architecture

```
+------------------+     +------------------+     +---------------------+
|   Work Unit      |     |   rESP           |     |   Verification      |
|   Registry       |---->|   Submission     |---->|   Engine            |
|                  |     |   Sink           |     |   (accept/reject)   |
|  register()      |     |  submit()        |     |  verify()           |
|  get()           |     |  submit_from_    |     |  match threshold    |
|  list()          |     |    detector()    |     |  triple-match ready |
+------------------+     +------------------+     +---------------------+
                                                           |
                                                           v
+------------------+     +------------------+     +---------------------+
|   FAM Adapter    |<----|   ROC            |<----|   Contribution      |
|   (emit only)    |     |   Scoring        |     |   Recording         |
|                  |     |                  |     |                     |
|  emit_contrib    |     |  score()         |     |  record()           |
|  _event()        |     |  complexity wt   |     |  get_stats()        |
|  NO direct       |     |  consistency     |     |                     |
|  core mutation   |     |  reward flag     |     |                     |
+------------------+     +------------------+     +---------------------+
        |
        v
  [ Downstream Distribution: MoltBook / Ledger / Token Hooks ]
```

---

## Integration Boundaries

| Boundary | Rule |
|---|---|
| FAMDaemon | Adapter only. No direct mutation of FAM event store |
| Core control-plane | No direct access unless sanctioned by interface |
| Contracts | All external-facing structures centralized in contracts.py |
| Interface | All callable surfaces documented in INTERFACE.md. No silent API sprawl |

---

## Current Phase

**Phase 0: Internal PoC** — COMPLETE
- Contracts defined, registry, submission sink, verification, contribution scoring
- 18/18 tests passing
- End-to-end flow: register -> submit -> verify -> record

**Phase 1: Internal Proto** — IN PROGRESS
- DetectorBridge wired to pqn_alignment.run_detector()
- Next: SQLite persistence, MoltBook publish adapter, participant gate, runbook

**Phase 2: Externalization Readiness** — PLANNED
- Interface freeze, standalone deploy path, dual-remote repo setup

**Phase 3: Spin-Out** — PLANNED
- This repo (science-swarm-hub) becomes the primary codebase
- Monorepo retains bridge/adapter stub only

---

## Repo Structure

```
science-swarm-hub/
├── README.md                    # This file
├── INTERFACE.md                 # Contract definitions and public API surface
├── docs/
│   ├── ARCHITECTURE.md          # System design and flow documentation
│   ├── EXFOLIATION_CHECKLIST.md # Proto spin-out trigger criteria
│   └── ONBOARDING.md           # External contributor onboarding guide
├── contracts/
│   └── contracts.py             # Reference contract dataclasses
├── examples/
│   └── workflow_example.py      # Example external workflow
└── tests/                       # (future) External integration tests
```

---

## Links

- **Active Build:** [Foundups-Agent/modules/foundups/pqn_swarm_hub](https://github.com/FOUNDUPS/Foundups-Agent/tree/main/modules/foundups/pqn_swarm_hub)
- **Integrated INTERFACE.md:** [Foundups-Agent INTERFACE](https://github.com/FOUNDUPS/Foundups-Agent/blob/main/modules/foundups/pqn_swarm_hub/INTERFACE.md)
- **Integrated ROADMAP.md:** [Foundups-Agent ROADMAP](https://github.com/FOUNDUPS/Foundups-Agent/blob/main/modules/foundups/pqn_swarm_hub/ROADMAP.md)

---

## License

MIT — See [LICENSE](./LICENSE)
