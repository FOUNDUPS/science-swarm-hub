# Migration Manifest - PQN Swarm Hub

**Status**: Phase 3 Prep (ready for 012 approval)
**Created**: 2026-03-29
**Slice**: `pqn_swarm_hub_phase3_prep_scaffold`

---

## Target Repositories

| Repo | Role | Visibility |
|------|------|------------|
| `FOUNDUPS/pqn-swarm-hub` | origin (org repo) | public |
| `Foundup/pqn-swarm-hub` | backup (personal repo) | private |

---

## Files to Migrate

### Product Code (src/)

| File | Lines | Disposition |
|------|-------|-------------|
| `src/__init__.py` | ~80 | MIGRATE |
| `src/contracts.py` | ~150 | MIGRATE |
| `src/registry.py` | ~100 | MIGRATE |
| `src/submission_sink.py` | ~120 | MIGRATE |
| `src/verification.py` | ~100 | MIGRATE |
| `src/contribution.py` | ~120 | MIGRATE |
| `src/gate.py` | ~300 | MIGRATE |
| `src/persistence.py` | ~400 | MIGRATE |
| `src/publication_adapter.py` | ~200 | MIGRATE |
| `src/fam_adapter.py` | ~150 | MIGRATE |
| `src/detector_bridge.py` | ~120 | MIGRATE |

**Total src/**: ~1,840 lines

### Tests (tests/)

| File | Tests | Disposition |
|------|-------|-------------|
| `tests/__init__.py` |  E| MIGRATE |
| `tests/README.md` |  E| MIGRATE |
| `tests/TestModLog.md` |  E| MIGRATE |
| `tests/test_contracts.py` | 13 | MIGRATE |
| `tests/test_detector_bridge.py` | 5 | MIGRATE |
| `tests/test_external_contributor.py` | 22 | MIGRATE |
| `tests/test_external_submission.py` | 14 | MIGRATE |
| `tests/test_fam_live_validation.py` | 15 | MIGRATE |
| `tests/test_persistence.py` | 18 | MIGRATE |
| `tests/test_poc_flow.py` | 5 | MIGRATE |
| `tests/test_publication_adapter.py` | 16 | MIGRATE |

**Total tests**: 108

### Documentation

| File | Disposition |
|------|-------------|
| `README.md` | MIGRATE |
| `INTERFACE.md` | MIGRATE |
| `ROADMAP.md` | MIGRATE |
| `ModLog.md` | MIGRATE |
| `CONTRIBUTING.md` | MIGRATE |
| `RUNBOOK.md` | MIGRATE |
| `requirements.txt` | MIGRATE |

### Root

| File | Disposition |
|------|-------------|
| `__init__.py` | MIGRATE |

---

## Files to Leave in Monorepo

### Bridge/Stub (Create New Post-Migration)

| File | Purpose |
|------|---------|
| `__init__.py` | Re-export stub pointing to `pqn_swarm_hub` package |
| `README.md` | Redirect notice to external repo |

### Historical Record (Keep)

| File | Purpose |
|------|---------|
| `PROTO_EXFOLIATION_CHECKLIST.md` | Migration audit trail |
| `MIGRATION_MANIFEST.md` | This file (reference) |
| `DUAL_REMOTE_PLAN.md` | Setup reference |
| `EXFOLIATION_PLAN.md` | Procedure reference |

---

## Standalone Repo Structure

```
pqn-swarm-hub/
├── README.md
├── INTERFACE.md
├── ROADMAP.md
├── ModLog.md
├── CONTRIBUTING.md
├── RUNBOOK.md
├── requirements.txt
├── setup.py (NEW - create for pip install)
├── pyproject.toml (NEW - modern packaging)
├── src/
━E  └── pqn_swarm_hub/
━E      ├── __init__.py
━E      ├── contracts.py
━E      ├── registry.py
━E      ├── submission_sink.py
━E      ├── verification.py
━E      ├── contribution.py
━E      ├── gate.py
━E      ├── persistence.py
━E      ├── publication_adapter.py
━E      ├── fam_adapter.py
━E      └── detector_bridge.py
├── tests/
━E  ├── __init__.py
━E  ├── README.md
━E  ├── TestModLog.md
━E  └── test_*.py (8 files)
└── .github/
    └── workflows/ (NEW - CI/CD)
```

---

## Monorepo Stub Structure (Post-Migration)

```

├── __init__.py           # Re-export: from pqn_swarm_hub import *
├── README.md             # Redirect notice
├── PROTO_EXFOLIATION_CHECKLIST.md  # Historical
├── MIGRATION_MANIFEST.md           # Historical
├── DUAL_REMOTE_PLAN.md             # Historical
└── EXFOLIATION_PLAN.md             # Historical
```

---

## Dependencies to Resolve

### Internal Dependencies (Adapter Strategy)

| Import | Source | Strategy |
|--------|--------|----------|
| `pqn_alignment.run_detector` | `modules/ai_intelligence/pqn_alignment/` | Adapter stub in standalone |
| `moltbook_distribution_adapter` | `modules/communication/moltbot_bridge/` | Adapter stub in standalone |
| `fam_daemon` | `modules/foundups/agent_market/` | Adapter stub in standalone |

### External Dependencies (requirements.txt)

```
# Core
dataclasses-json>=0.6.0

# Persistence
# (uses stdlib sqlite3)

# Testing
pytest>=8.0.0
pytest-asyncio>=1.3.0
```

---

## Migration Checklist

### Pre-Migration (This Slice)

- [x] MIGRATION_MANIFEST.md created
- [x] DUAL_REMOTE_PLAN.md created
- [x] EXFOLIATION_PLAN.md created
- [ ] 012 approval obtained

### Migration Execution (012 Approval Required)

- [ ] Create `FOUNDUPS/pqn-swarm-hub` repo
- [ ] Create `Foundup/pqn-swarm-hub` repo
- [ ] Clone fresh, copy files per manifest
- [ ] Create `setup.py` / `pyproject.toml`
- [ ] Create adapter stubs for internal deps
- [ ] Verify tests pass in standalone
- [ ] Push to both remotes
- [ ] Update monorepo stub

### Post-Migration

- [ ] Verify pip installable
- [ ] Update monorepo to import from package
- [ ] Tag first release (v0.11.0 or v1.0.0)
- [ ] Update FOUNDUP_EXFOLIATION_PROTOCOL.md

---

*Created: 2026-03-29*

