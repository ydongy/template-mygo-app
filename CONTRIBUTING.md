# Contributing

Thanks for helping. Agent and repository rules are in [AGENTS.md](AGENTS.md).

- Issues and pull requests may be written in English or Simplified Chinese.
- Open an issue before a large change so we can agree on the direction first. Small fixes can go straight to a
  pull request.
- Do not report vulnerabilities in public issues; use **Security → Report a vulnerability** on GitHub.

## Development setup

Requirements: the Go version in `.go-version`, Python 3 for the helper scripts. No Node, Bun or WebView.

```bash
scripts/check.sh --cross     # gofmt, go mod tidy, vet, tests, script tests, cross-compilation
go test -race ./...
go tool mygo dev             # run the app
go tool mygo build           # package locally
```

CI (`.github/workflows/ci.yml`) runs `scripts/check.sh --cross`, `python3 scripts/scan_secrets.py` over the whole
history and `go test -race ./...` on every pull request and push to `main`.

## Commits, branches and pull requests

- Commit messages and pull request titles follow [Conventional Commits](https://www.conventionalcommits.org/):
  `feat|fix|docs|refactor|perf|test|build|ci|chore|revert(scope)!: subject`.
- Name branches `<type>/<issue>-<slug>`, for example `fix/12-counter-reset`.
- The maintainer squash-merges, so the pull request title becomes the commit message. No DCO or sign-off is
  required.
- Keep a change focused, add or update tests, and add a line under `## [Unreleased]` in `CHANGELOG.md` when users
  would notice it.
- Put screenshots in the pull request body, not in the repository.
