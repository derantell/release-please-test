# CLAUDE.md

## Project Structure

This is a monorepo with 4 independently versioned packages, used to test release-please workflows.

```
packages/
  api-server/      Node.js Express API      (release-type: node)
  web-client/      Node.js frontend client   (release-type: node)
  core-lib/        C#/.NET class library     (release-type: simple + extra-files)
  data-processor/  Python data pipeline      (release-type: python)
```

## Configuration Files

- `release-please-config.json` — defines packages, their release types, and changelog settings
- `.release-please-manifest.json` — tracks current version of each package
- `.github/workflows/release-please.yml` — GitHub Actions workflow that runs on push to main

## Release-Please Workflow

Release-please uses Conventional Commits to determine version bumps and generate changelogs.

### Commit Format

Commits must follow Conventional Commits to trigger releases:

```
<type>(<scope>): <description>
```

- `feat` → minor version bump (or patch while < 1.0.0 due to `bump-minor-pre-major`)
- `fix` → patch version bump
- `feat!` or `BREAKING CHANGE:` footer → major version bump (or minor while < 1.0.0)

### Scoping Commits to Packages

Release-please detects affected packages by file paths, not commit scopes. A commit that changes files under `packages/api-server/` will only trigger a release for api-server.

The scope in the commit message (e.g., `feat(api-server): ...`) is used for changelog readability, not for package detection.

### How Releases Happen

1. Push conventional commits to `main`
2. Release-please opens a PR per affected package (due to `separate-pull-requests: true`)
3. The PR updates CHANGELOG.md, version in the package manifest, and `.release-please-manifest.json`
4. Merging the PR creates a GitHub release with a git tag

### Version Files Per Language

Each release type knows which files contain version numbers:

- **node**: `package.json`
- **python**: `pyproject.toml`, `__init__.py` (`__version__`)
- **simple** (core-lib): `version.txt` + `.csproj` `<Version>` via extra-files xpath

## Commands

- Run Python library: `cd packages/data-processor && python3 -c "from src.data_processor.pipeline import Record, transform; print(transform([Record(1, 'hello')]))"`
- Run Node API: `cd packages/api-server && npm install && npm start`
