<!-- template: process.md v1 -->
# Template development process

The process is https://github.com/ydongy/.github/tree/6b48552c969c28a954498123bb502a556f8eed79/handbook.
This file lists only the template-specific details.

## Commit scopes and labels

`app`, `example`, `i18n`, `scripts`, `docs`, `ci`.

## Contracts

Version and packaging in mygo.json; locale selection and embedded catalog in the example package.
The example is a neutral fixture, not a product screen approval.

## CI

The docs workflow and handbook link pin the same ydongy/.github revision. Upgrade both explicitly;
changes to the shared handbook on main do not alter this repository's checks.

Calls mygo-ci.yml and docs-check.yml. The shared CI scans Git history for credential patterns. The manual packaging workflow saves unsigned/development
artifacts only. Run scripts/check.sh --cross locally; hosted CI depends on the handbook changes landing.

## History

Created as a pure Go native template. No product-specific history.
