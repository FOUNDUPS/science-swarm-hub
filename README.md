# Science Swarm Hub

**Status**: Standalone release-ready (v0.12.0)
**Package**: `pqn_swarm_hub`
**License**: MIT

---

## Purpose

Science Swarm Hub coordinates bounded research work units, result submissions, verification decisions, and contribution measurement. It is the operational core of the PQN Swarm Hub FoundUp.

The system rewards **verified contribution**, not narrative activity.

### Capabilities

- **Work Registry**: Register bounded research tasks (PQNWorkUnit)
- **Submission Sink**: Intake structured results (rESPSubmission)
- **Verification Engine**: Accept/reject decisions with audit trail (VerificationDecision)
- **Contribution Reporter**: ROC-style contribution measurement (ContributionRecord)
- **Participant Gate**: Entry policy enforcement with tier system
- **SQLite Persistence**: Durable storage across restarts

---

## Installation

```bash
# From PyPI (when published)
pip install science-swarm-hub

# From source
git clone https://github.com/FOUNDUPS/science-swarm-hub.git
cd science-swarm-hub
pip install -e .

# With test dependencies
pip install -e .[test]
```

### Verify Installation

```python
from pqn_swarm_hub import WorkUnitRegistry, SubmissionSink
print("Install OK")
```

---

## Quick Start

```python
from pqn_swarm_hub import (
    WorkUnitRegistry,
    SubmissionSink,
    VerificationEngine,
    ContributionReporter,
)

# Setup services (in-memory)
registry = WorkUnitRegistry()
sink = SubmissionSink(registry)
engine = VerificationEngine(sink)
reporter = ContributionReporter(engine)

# 1. Register work unit
work_unit = registry.register(
    description="7.05Hz resonance sweep",
    config={"steps": 1200, "dt": 0.071},
    creator_id="agent_x",
)

# 2. Submit result
submission = sink.submit(
    work_unit_id=work_unit.work_unit_id,
    submitter_id="agent_x",
    metrics={"coherence": 0.74, "pqn_rate": 0.12},
)

# 3. Verify (auto-accept if coherence >= 0.618)
decision = engine.auto_verify(submission.submission_id)

# 4. Record contribution (if accepted)
if decision.decision == "accept":
    contribution = reporter.record(
        work_unit_id=work_unit.work_unit_id,
        submission_id=submission.submission_id,
        decision_id=decision.decision_id,
        contributor_id="agent_x",
        score=0.85,
    )
    print(f"Contribution: {contribution.contribution_id}")
```

---

## With Persistence

```python
from pqn_swarm_hub import (
    WorkUnitRegistry,
    SubmissionSink,
    VerificationEngine,
    ContributionReporter,
    get_sqlite_store,
)

# Get shared SQLite store (creates data/pqn_swarm_hub/swarm.db)
store = get_sqlite_store()

# Wire services with persistence
registry = WorkUnitRegistry(store=store)
sink = SubmissionSink(registry, store=store)
engine = VerificationEngine(sink, store=store)
reporter = ContributionReporter(engine, store=store)

# All operations now persist to SQLite
```

---

## Running Tests

```bash
# All tests
pytest tests/ -v

# Quick run
pytest tests/ -q
# Expected: 108 passed
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [INTERFACE.md](INTERFACE.md) | Public API contracts and integration points |
| [RUNBOOK.md](RUNBOOK.md) | Reproducible execution guide |
| [CONTRIBUTING.md](CONTRIBUTING.md) | External contributor guide |
| [ROADMAP.md](ROADMAP.md) | Phase plan and success metrics |
| [ModLog.md](ModLog.md) | Change history |

---

## Requirements

- Python 3.12+
- No external dependencies (stdlib only)

---

## License

MIT License - see [LICENSE](LICENSE) for details.
