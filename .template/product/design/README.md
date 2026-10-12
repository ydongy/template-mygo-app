# Design mockups

The design language is [docs/design.md](../docs/design.md); its spacing, size and color values are in
[tokens.md](tokens.md). Mockups are self-contained HTML pages with no external resources and illustrate the template
fixture, not real device captures:

- `screens/example.html` is interactive: `?state=zero|positive|negative` shows one state and `?scheme=light|dark`
  forces the color scheme.
- `screens/example-appearance.html` shows the example in light and dark side by side, with focus rings.

`screens/<screen>.html` is implemented by `internal/ui/<screen>/`; the mockup's text and states are that package's
`copy.json` and screen states.

## Working rules

A UI change starts from the mockup: edit or add `screens/<screen>.html` (light and dark, every state), get the visual
direction confirmed by the maintainer, then write the native view in `internal/ui/<screen>/` with theme roles,
localized copy, accessible names and tests. Change the design text (`docs/design.md`, `tokens.md`) and the native view
together. A headless test is not device acceptance. Commit only real device captures as screenshots.
