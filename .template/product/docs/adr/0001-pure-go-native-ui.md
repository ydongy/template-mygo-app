<!-- template: adr.md v1 -->
# 0001 Pure Go native UI

- Status: accepted
- Date: 2026-10-07
- Related: `docs/spec.md#technical-baseline`

## Context

The template needs a native desktop UI with a single language and reproducible builds.
Reference: [native UI guide](https://mygo.egoist.dev/docs/ui) and
[the pinned MyGo source](https://github.com/egoist/mygo/tree/v0.2.16).

## Decision

Use MyGo native UI, one Go module and a module-pinned CLI. Use the native updater plugin.

## Cost

GPU-rendered controls require device accessibility and platform testing. MyGo is at an early
version; pinned upgrades require reviewing API and packaging changes.

## Revisit triggers

A required platform capability or accessibility contract cannot be met by native UI.
