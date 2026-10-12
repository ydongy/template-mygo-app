# Contributing

Template is closed source; this guide is for the maintainer, collaborators and any future contributor. Open an
issue before a large change so the direction is agreed first.

## Development setup

Requirements: the Go version in `.go-version`, Python 3 for the helper scripts. No Node, Bun or WebView.

```bash
scripts/check.sh --cross     # gofmt, go mod tidy, vet, tests, script tests, cross-compilation
go test -race ./...
python3 scripts/scan_secrets.py
go tool mygo dev             # run the app
go tool mygo build           # package locally
```

## Commits, branches and pull requests

- Commit messages and pull request titles follow [Conventional Commits](https://www.conventionalcommits.org/):
  `feat|fix|docs|refactor|perf|test|build|ci|chore|revert(scope)!: subject`. The scope is optional; usual ones:
  `app`, `example`, `i18n`, `scripts`, `docs`, `ci`. `pr-title.yml` checks the title.
- Name branches `<type>/<issue>-<slug>`, for example `fix/12-counter-reset`.
- The maintainer squash-merges. No sign-off is required.
- A UI change starts from the mockup in `design/screens/`; the maintainer confirms the visual direction before UI
  code is written.
- Keep a change focused and add or update tests.

## Changelog

`CHANGELOG.md` (English) and `CHANGELOG.zh.md` (Chinese) carry the same bullets under `## [Unreleased]`. Write what
a user would notice, with no issue or PR numbers, hashes or tooling words. The Chinese file feeds the changelog
page of the product website, which is why it stays.

## Releasing

`python3 scripts/bump.py <version>` sets the version in `mygo.json` and dates `[Unreleased]` in both changelogs.
Every released version has a security review in `docs/security/`. The release steps and what is not yet automated
are in [docs/releasing.md](docs/releasing.md).
