# EXFOLIATION CHECKLIST — Science Swarm Hub FoundUp

> Proto spin-out trigger criteria. All items must pass before this repo becomes the primary codebase.

---

## Overview

The Science Swarm Hub is currently built as an integrated module inside Foundups-Agent at `modules/foundups/pqn_swarm_hub/`. This checklist defines the criteria that must be met before exfoliating (spinning out) to this standalone repo.

**Exfoliation target:** Phase 3 (Spin-Out)
**Current phase:** Phase 1 (Internal Proto)

---

## Phase 1 Completion Gates

- [ ] All Phase 1 slices implemented and tested
  - [x] Slice 1: Registry (work unit registration and retrieval)
  - [x] Slice 2: rESP Sink (structured result intake)
  - [x] Slice 3: Verification (accept/reject logic with phi-floor)
  - [x] Slice 4: ROC (contribution scoring with durable artifacts)
  - [ ] Slice 5: Participant Gate (entry policy enforcement)
  - [x] Slice 6: Detector Bridge (pqn_alignment integration)
- [ ] SQLite persistence for all contracts
- [ ] MoltBook distribution adapter wired
- [ ] Reproducible runbook documented

## FAMDaemon Integration

- [ ] FAM adapter implemented (emit-only)
- [ ] Contribution events flowing through adapter
- [ ] No direct core mutation confirmed
- [ ] Audit-safe output structure verified

## Work Unit Coverage

- [ ] 3+ work unit types supported and tested
- [ ] Different detector configurations exercised
- [ ] Edge cases handled (cancellation, duplicate submission, invalid config)

## External Contributor Path

- [ ] External contributor can discover work units via documented API
- [ ] External contributor can submit results via documented API
- [ ] Verification works for external submissions
- [ ] Contribution scoring works for external participants
- [ ] Gate enforces entry policy for external participants

## Contract Stability

- [ ] Contracts stable enough to freeze (no breaking changes for 2+ weeks)
- [ ] All four core contracts finalized: PQNWorkUnit, rESPSubmission, VerificationDecision, ContributionRecord
- [ ] INTERFACE.md matches actual implementation
- [ ] No undocumented API surfaces

## Independence Requirements

- [ ] No core Foundups-Agent changes required for external PRs
- [ ] Module can run with adapter stubs (no hard dependency on FAMDaemon)
- [ ] DetectorBridge can be reconfigured for API-based detector calls
- [ ] No hidden imports from unrelated Foundups-Agent modules
- [ ] All shared touchpoints documented

## Repo Readiness

- [ ] science-swarm-hub repo structure matches target layout
- [ ] README, INTERFACE, ARCHITECTURE docs current
- [ ] CI/CD pipeline configured
- [ ] Contribution guidelines (CONTRIBUTING.md) written
- [ ] Dual-remote setup documented (FOUNDUPS/science-swarm-hub + Foundup/science-swarm-hub)

---

## Spin-Out Procedure (when all gates pass)

1. Migrate product code from `modules/foundups/pqn_swarm_hub/` to this repo
2. Leave monorepo bridge/adapter stub in Foundups-Agent
3. Create Foundup/science-swarm-hub as backup remote
4. Verify standalone deployment with adapter stubs
5. Confirm independent release cadence is possible
6. Archive integrated module path (keep stub only)

---

## Status

**Last reviewed:** Not yet reviewed
**Blocker count:** TBD
**Estimated readiness:** Phase 2 completion
