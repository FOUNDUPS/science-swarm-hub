# Seed Issue: Add development setup section to README

**Type**: Task
**Labels**: documentation, good first issue
**Title**: [Task] Add development setup section to README.md

## Summary

README.md has installation instructions but no explicit development setup guide for contributors who want to run tests locally or make changes.

## Current State

README shows:
- `pip install -e .` (basic)
- `pip install -e .[test]` (with test deps)
- `pytest tests/ -v`

Missing:
- Explicit "Development Setup" section
- Virtual environment recommendation
- Pre-commit or lint info (if any)
- How to run specific test files

## Proposed Addition

Add a "Development Setup" section after "Installation":

```markdown
## Development Setup

```bash
# Clone and setup
git clone https://github.com/FOUNDUPS/science-swarm-hub.git
cd science-swarm-hub
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -e .[test]

# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_external_submission.py -v

# Run with coverage
pytest tests/ --cov=pqn_swarm_hub --cov-report=term-missing
```
```

## Acceptance Criteria

- [ ] README has "Development Setup" section
- [ ] Virtual environment setup included
- [ ] Coverage command with correct package name
- [ ] Windows activation noted

## Why This Matters

Clear dev setup reduces onboarding friction for first-time contributors.
