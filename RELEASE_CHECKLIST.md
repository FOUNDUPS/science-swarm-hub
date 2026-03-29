# Release Checklist - Science Swarm Hub

## Pre-Release Verification

### Code Quality

- [ ] All tests pass: `pytest tests/ -v` (expect 108 passed)
- [ ] Import verification: `python -c "from pqn_swarm_hub import WorkUnitRegistry"`
- [ ] Smoke test passes (see RUNBOOK.md Section 5)

### Documentation

- [ ] README.md has correct version number
- [ ] INTERFACE.md reflects current API
- [ ] RUNBOOK.md examples work
- [ ] CONTRIBUTING.md is up to date
- [ ] ModLog.md has entry for this release

### Package Metadata

- [ ] `pyproject.toml` version matches release tag
- [ ] License file present
- [ ] Authors/maintainers correct

---

## Release Process

### 1. Version Bump

```bash
# Update version in pyproject.toml
# Update version in README.md status line
# Add ModLog.md entry
```

### 2. Final Verification

```bash
cd /path/to/science-swarm-hub
pip install -e .[test]
pytest tests/ -v
```

### 3. Commit and Tag

```bash
git add .
git commit -m "release: v0.X.Y

- [summary of changes]

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
"

git tag -a v0.X.Y -m "Release v0.X.Y"
```

### 4. Push

```bash
# Push to both remotes
git push origin main --tags
git push backup main --tags
```

### 5. GitHub Release (Optional)

```bash
gh release create v0.X.Y --title "v0.X.Y" --notes "Release notes here"
```

### 6. PyPI Publish (Future)

```bash
# Build
python -m build

# Upload to PyPI
python -m twine upload dist/*
```

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| v0.12.0 | 2026-03-30 | Standalone release-ready |

---

*Last Updated: 2026-03-30*
