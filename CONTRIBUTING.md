# Contributing

Thanks for helping. Open an issue before a large change so we can agree on the direction first.

## Development setup

Requirements: the Go version in `.go-version`, Python 3 for the helper scripts. No Node, Bun or WebView.

```bash
scripts/check.sh --cross     # gofmt, go mod tidy, vet, tests, script tests, cross-compilation
go test -race ./...
go tool mygo dev             # run the app
go tool mygo build           # package locally
```

## Commits, branches and pull requests

- Commit messages and pull request titles follow [Conventional Commits](https://www.conventionalcommits.org/):
  `feat|fix|docs|refactor|perf|test|build|ci|chore|revert(scope)!: subject`.
- Name branches `<type>/<issue>-<slug>`, for example `fix/12-counter-reset`.
- The maintainer squash-merges. No sign-off is required.
- Keep a change focused, add or update tests, and add a line under `## [Unreleased]` in `CHANGELOG.md` when users
  would notice it.
