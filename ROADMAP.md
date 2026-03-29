# ROADMAP - PQN Swarm Hub FoundUp

## Phase Plan (per Exfoliation Protocol)

### Phase 0: Internal PoC (COMPLETE)

**Goal**: Minimal scaffold with explicit contracts and one end-to-end flow.

**Deliverables**:
- [x] Module structure (README, INTERFACE, ROADMAP, ModLog)
- [x] PoC contracts defined (PQNWorkUnit, rESPSubmission, VerificationDecision, ContributionRecord)
- [x] `src/contracts.py` with dataclasses
- [x] `src/registry.py` with in-memory work unit registry
- [x] `src/submission_sink.py` with rESP intake
- [x] `src/verification.py` with accept/reject logic (ρEfloor 0.618, manual override)
- [x] `src/contribution.py` with ROC reporting + durable JSON artifact
- [x] One end-to-end PoC path (register -> submit -> verify -> record)  E18/18 tests pass
- [x] Basic tests for contracts and flows

**Acceptance Criteria**: ALL MET

---

### Phase 1: Internal Proto (COMPLETE)

**Goal**: Wire to shared infrastructure and prove reproducible runbook.

**Deliverables**:
- [x] SQLite persistence for contracts  E`src/persistence.py` with store injection
- [x] Integration with pqn_alignment detector via API calls  E`DetectorBridge` + `submit_from_detector()`
- [x] Integration with moltbook_distribution_adapter for downstream publish  E`src/publication_adapter.py`
- [x] Participant gate (who can submit to this FoundUp)  E`src/gate.py`
- [x] Reproducible runbook documented  E`RUNBOOK.md`
- [x] Adapter boundaries to shared infrastructure documented  E`src/fam_adapter.py` + `INTERFACE.md`

**Acceptance Criteria**:
- Work units persist across restarts
- Detector results flow through submission sink
- Verified contributions publish to MoltBook
- Gate enforces participant entry policy
- Another 012/Claw can participate through stable boundaries

---

### Phase 2: Externalization Readiness (COMPLETE)

**Goal**: Complete externalization gates and lock interfaces.

**Entry Approved**: 2026-03-29 (proto-readiness review)
**Phase Complete**: 2026-03-29 (exfoliation review decision)

**Deliverables**:
- [x] Live FAMDaemon validation  E`pqn_swarm_hub_fam_live_validation` (15/15 tests)
- [x] Generic external submission type  E`pqn_swarm_hub_external_submission_type` (14/14 tests)
- [x] External contributor path  E`pqn_swarm_hub_external_contributor_path` (22/22 tests)
- [x] Interfaces frozen (except V3 consensus  Efuture scope)
- [x] Standalone deploy path verified (RUNBOOK.md + stub-safe adapters)
- [ ] Dual-remote repo setup prepared  E**Phase 3 scope**
- [x] Monorepo stub/adapter strategy documented (PROTO_EXFOLIATION_CHECKLIST.md)

**True Blockers for Exfoliation**: ALL CLEARED
1. ~~FAMAdapter live test with actual FAMDaemon~~  ECOMPLETE
2. ~~Generic external submission work-unit type~~  ECOMPLETE
3. ~~CONTRIBUTING.md + entry gate test with external identity~~  ECOMPLETE

**Not Blockers** (optional/future):
- GPD work unit type (separate bootstrap lane)
- V3 consensus schema (Shapley/ZK)

**Acceptance Criteria**: ALL MET
- FAM events appear in live FAM store ✁E
- External submission type tested (14 tests) ✁E
- External contributor can request entry (22 tests) ✁E
- No interface-breaking changes after freeze ✁E
- Module can deploy independently (with adapter stubs) ✁E
- Migration path to `FOUNDUPS/PQNSwarmHub` documented ✁E

---

### Phase 3: Spin-Out (PREP COMPLETE)

**Goal**: Externalize to standalone FoundUp repo.

**Phase 3 Prep** (2026-03-29):
- [x] `MIGRATION_MANIFEST.md`  Efile disposition list
- [x] `DUAL_REMOTE_PLAN.md`  Erepo setup commands
- [x] `EXFOLIATION_PLAN.md`  Efull procedure with rollback
- [ ] 012 approval for execution  E**PENDING**

**Migration Deliverables** (blocked on 012):
- [ ] Create `FOUNDUPS/pqn-swarm-hub` as origin
- [ ] Create `Foundup/pqn-swarm-hub` as backup
- [ ] Migrate product code per manifest
- [ ] Create adapter stubs for internal deps
- [ ] Leave monorepo stub pointing to external package

**Acceptance Criteria**:
- Standalone repo operational
- All 108 tests pass standalone
- Monorepo stub imports from external package
- Independent release cadence possible

---

## Current Execution Priority

**Phase 0**: COMPLETE (scaffold @ 35d1e2275)

**Phase 1 Progress**: COMPLETE
- [x] `pqn_swarm_hub_detector_bridge`  EDetectorBridge wires pqn_alignment.run_detector() into submission flow
- [x] `pqn_swarm_hub_gate`  EParticipantGate with tier system, policy hooks, internal-first auto-approve
- [x] `pqn_swarm_hub_fam_adapter`  EFAMAdapter with emit_contribution_event(), stub fallback
- [x] `pqn_swarm_hub_persistence`  ESQLiteStore with optional store injection (41/41 tests pass)
- [x] `pqn_swarm_hub_publication_adapter`  EPublicationAdapter wraps MoltBook, stub-safe (57/57 tests pass)
- [x] `pqn_swarm_hub_runbook`  EReproducible execution guide in `RUNBOOK.md`

**Phase 2**: COMPLETE (2026-03-29 exfoliation review decision)

**Phase 2 Slices** (all complete):
1. ~~`pqn_swarm_hub_fam_live_validation`~~  ECOMPLETE (15/15 tests)
2. ~~`pqn_swarm_hub_external_submission_type`~~  ECOMPLETE (14/14 tests)
3. ~~`pqn_swarm_hub_external_contributor_path`~~  ECOMPLETE (22/22 tests)

**Total tests**: 108 passing

**Phase 3 Prep**: COMPLETE (migration scaffold ready)

**Next action**: 012 approval for repo creation and migration execution

---

## Success Metrics

### Phase 0
- Contracts compile and import cleanly
- One end-to-end flow executes without error
- Reuse of pqn_alignment detector works

### Phase 1
- Persistence survives restart
- MoltBook publish succeeds
- Gate blocks unauthorized participants

### Phase 2
- Zero interface changes after freeze
- Standalone deploy smoke test passes

### Phase 3
- External repo accepts PRs
- Independent release shipped

