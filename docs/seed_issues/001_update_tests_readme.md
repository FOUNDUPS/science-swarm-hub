# Seed Issue: Update tests/README.md

**Type**: Task
**Labels**: good first issue, documentation
**Title**: [Task] Update tests/README.md to reflect current test structure

## Summary

The `tests/README.md` is outdated. It references files that don't exist and has incorrect paths.

## Current State

- Lists `test_registry.py`, `test_submission.py`, etc. as "(future)" but they don't exist
- Coverage path references old monorepo path: `modules.foundups.pqn_swarm_hub`
- Doesn't list the actual test files that exist

## Actual Test Files

```
tests/
  test_contracts.py
  test_detector_bridge.py
  test_external_contributor.py
  test_external_submission.py
  test_fam_live_validation.py
  test_persistence.py
  test_poc_flow.py
  test_publication_adapter.py
```

## Acceptance Criteria

- [ ] `tests/README.md` lists actual test files
- [ ] Coverage command uses correct path: `--cov=pqn_swarm_hub`
- [ ] Remove "(future)" references to non-existent files
- [ ] Keep running instructions accurate

## Why This Matters

New contributors read `tests/README.md` to understand test structure. Outdated info creates friction.
