# INTERFACE — PQN Swarm Hub FoundUp

> Reference contract definitions and public API surface for external contributors.
> Synced from: `Foundups-Agent/modules/foundups/pqn_swarm_hub/INTERFACE.md`

---

## Canonical Split

| Module | Responsibility |
|---|---|
| OpenClaw (0102) | Conversational research control plane |
| pqn_swarm_hub | Work registry, verification, contribution measurement |
| pqn_alignment | Detector-first execution engine |
| pqn_mcp | Gated external/tool surface |
| pqn_portal | Public demo/gallery |
| moltbook_distribution_adapter | Downstream distribution |

This module is the FoundUp-level registry and verification layer. It does NOT own the detector engine or the social distribution layer.

---

## Contracts

### PQNWorkUnit

Bounded research task registration.

```python
@dataclass
class PQNWorkUnit:
    work_unit_id: str          # Deterministic ID
    description: str           # Human-readable description
    config: Dict[str, Any]     # CMST detector config (steps, dt, seed, etc.)
    creator_id: str            # Agent/user who created this work unit
    status: WorkUnitStatus     # pending, in_progress, completed, cancelled
    created_at: datetime
    updated_at: datetime
```

### rESPSubmission

Structured rESP result intake.

```python
@dataclass
class rESPSubmission:
    submission_id: str         # Deterministic ID
    work_unit_id: str          # Reference to parent work unit
    submitter_id: str          # Agent/user who submitted
    metrics: Dict[str, Any]    # {coherence, pqn_rate, paradox_rate, resonance_hz}
    artifacts: List[str]       # Paths or URIs to result artifacts
    status: SubmissionStatus   # pending_verification, accepted, rejected
    submitted_at: datetime
```

### VerificationDecision

Accept/reject outcome.

```python
@dataclass
class VerificationDecision:
    decision_id: str           # Deterministic ID
    submission_id: str         # Reference to submission
    decision: Literal["accept", "reject"]
    verifier_id: str           # Agent/user who made decision
    rationale: str             # Why accepted/rejected
    decided_at: datetime
```

### ContributionRecord

ROC-style contribution output.

```python
@dataclass
class ContributionRecord:
    contribution_id: str       # Deterministic ID
    work_unit_id: str          # Reference to work unit
    submission_id: str         # Reference to submission
    decision_id: str           # Reference to verification decision
    contributor_id: str        # Who earned the contribution
    score: float               # 0.0-1.0 contribution score
    recorded_at: datetime
```

---

## Public API Functions

### Work Unit Registry

- `register_work_unit(description, config, creator_id)` -> PQNWorkUnit
- `get_work_unit(work_unit_id)` -> Optional[PQNWorkUnit]
- `list_work_units(status_filter, limit)` -> List[PQNWorkUnit]
- `cancel_work_unit(work_unit_id, actor_id)` -> bool

### rESP Submission Sink

- `submit(work_unit_id, submitter_id, metrics, artifacts)` -> rESPSubmission
- `submit_from_detector(work_unit_id, bridge_result, submitter_id)` -> rESPSubmission
- `get_submission(submission_id)` -> Optional[rESPSubmission]
- `list_submissions(work_unit_id, status_filter, limit)` -> List[rESPSubmission]

### Verification

- `verify_submission(submission_id, decision, verifier_id, rationale)` -> VerificationDecision
- `get_decision(decision_id)` -> Optional[VerificationDecision]
- `list_decisions(submission_id)` -> List[VerificationDecision]

### Contribution Reporting

- `record_contribution(work_unit_id, submission_id, decision_id, contributor_id, score)` -> ContributionRecord
- `get_contribution(contribution_id)` -> Optional[ContributionRecord]
- `list_contributions(contributor_id, limit)` -> List[ContributionRecord]
- `get_contributor_stats(contributor_id)` -> Dict[str, Any]

---

## Deterministic ID Generation

All IDs are deterministic for idempotency:

```python
def generate_id(entity_type: str, *args: str) -> str:
    seed = f"{entity_type}:{':'.join(args)}"
    return hashlib.sha256(seed.encode()).hexdigest()[:16]
```

---

## Error Handling

| Error | Condition |
|---|---|
| WorkUnitNotFoundError | work_unit_id does not exist |
| SubmissionNotFoundError | submission_id does not exist |
| InvalidStatusTransitionError | Attempting invalid status transition |
| DuplicateSubmissionError | Submitting duplicate result (idempotent - returns existing) |

---

## Integration Points

### Detector Engine (via DetectorBridge)

DetectorBridge wires pqn_alignment.run_detector() into the submission flow.

### Downstream Distribution (MoltBook)

Verified contributions can be published to MoltBook via the distribution adapter.

---

## Adapter Boundary Rules

1. FAMDaemon integration MUST go through adapter only
2. Allowed: emit_contribution_event(ContributionRecord)
3. NOT allowed: direct mutation of FAM event store or core control-plane modules
