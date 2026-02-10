# release-please-test

A test monorepo for experimenting with [release-please](https://github.com/googleapis/release-please) — Google's tool for automating versioning, changelogs, and GitHub releases using Conventional Commits.

## What's in here

Four small packages across three languages, each with independent versioning:

| Package | Language | Path |
|---------|----------|------|
| api-server | Node.js | `packages/api-server` |
| web-client | Node.js | `packages/web-client` |
| core-lib | C# / .NET 8 | `packages/core-lib` |
| data-processor | Python | `packages/data-processor` |

The packages themselves are intentionally trivial. The point is testing the release tooling, not the code.

## How it works

1. Write code and commit to `main` using [Conventional Commits](https://www.conventionalcommits.org/)
2. Release-please detects which packages were changed based on file paths
3. It opens a release PR per package that updates the version and changelog
4. Merging the PR creates a GitHub release with a tag

### Commit examples

```bash
# Triggers a release for api-server
git commit -m "feat(api-server): add pagination to items endpoint"

# Triggers a release for core-lib
git commit -m "fix(core-lib): handle division by zero edge case"

# Breaking change — bumps major version (or minor while pre-1.0)
git commit -m "feat(data-processor)!: change Record field names"
```

## Configuration

| File | Purpose |
|------|---------|
| `release-please-config.json` | Package definitions, release types, changelog sections |
| `.release-please-manifest.json` | Current version of each package |
| `.github/workflows/release-please.yml` | GitHub Actions workflow |

All packages start at version `0.1.0`. While below `1.0.0`, breaking changes bump the minor version instead of major (`bump-minor-pre-major: true`).

## Setup

No setup needed beyond pushing to GitHub. The workflow runs automatically on pushes to `main`.
