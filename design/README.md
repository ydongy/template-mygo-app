<!-- template: design-README.md v2 -->
# Design mockups

## Viewing

Open screens/example.html in a browser. It illustrates the template fixture, not real device captures.
Use ?state=zero,positive,negative and ?scheme=light,dark to inspect states.

## Screens

| Screen | Spec | Design file | Code dir | Status | Signed off | Accepted |
|---|---|---|---|---|---|---|
| Example | `docs/spec.md#counting` | `screens/example.html` | `internal/ui/example/` | planned | | |

## Decision log

2026-10-07: maintainer chose pure Go native UI. The neutral example has no screen sign-off
or device acceptance; initialized products replace it and follow the design gates.

## Maintenance

Change spec, design text and native view together. The fixture does not advance the ledger.
Real products obtain explicit review and commit only real device captures.
