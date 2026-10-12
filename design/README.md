# Design

Mockups and design notes for the native UI. The design language is [docs/design.md](../docs/design.md); the values it
uses are in [tokens.md](tokens.md).

## Layout

| Path | Purpose |
|---|---|
| `screens/<screen>.html` | One self-contained mockup per screen: static HTML and CSS, no external resources |
| `screens/example-appearance.html` | The example screen side by side in light and dark, with focus rings |
| `tokens.md` | Spacing, size, color and motion values, mapped to MyGo theme roles |

## Viewing

Open a file in `screens/` in a browser. These illustrate the template fixture and are not device captures.
`screens/example.html` is interactive: `?state=zero|positive|negative` shows one state and `?scheme=light|dark`
forces the color scheme.
`screens/example-appearance.html` needs no query.

## Screens

| Screen | Design file | Code dir | Status |
|---|---|---|---|
| Example | `screens/example.html`, `screens/example-appearance.html` | `internal/ui/example/` | fixture |

A mockup maps to a package: `screens/<screen>.html` is implemented by `internal/ui/<screen>/`. The text and states in
the mockup are the strings in that package's `copy.json` and the states its `Screen` can be in; the test in the
package covers each state.

## Changing the UI

1. Edit or add the mockup in `screens/` (light and dark, every state, the longest translation if layout is at risk)
   and update `tokens.md` and `docs/design.md` if a rule changes.
2. The maintainer confirms the visual direction. Do not write UI code before this.
3. Write the native view in `internal/ui/<screen>/` with theme roles and `Space`/`Rem` sizes, localized copy and
   accessible names, plus tests.
4. Run `scripts/check.sh`, then the acceptance checklist in `docs/design.md` on real devices. A headless test is not
   device acceptance.

Commit only real device captures as screenshots.

## Decision log

2026-10-07: maintainer chose pure Go native UI. The neutral example has no screen sign-off or device acceptance;
replace it with your own screens.
