# Template design language

This is the design language of `Template`: the rules every screen follows, and the place to record where a product
departs from them. It builds on the native UI toolkit of [MyGo](https://github.com/egoist/mygo) and summarizes the
parts of its [UI guides](https://github.com/egoist/mygo/blob/main/docs/ui/README.md) that matter for design; the
guides stay the authority on API details. The links below point to the upstream `main` branch; the toolkit version
this template builds against is pinned in `go.mod` (v0.2.16), so check a page against that version before relying on
an API it describes.

The counter in `internal/ui/example/` is a neutral fixture that demonstrates these rules. Replace it with your own
screens and edit this document to match.

Related files: [design/README.md](../design/README.md) (mockups and the UI change process) and
[design/tokens.md](../design/tokens.md) (spacing, size and color values in one table).

## Contents

1. [Principles](#principles)
2. [Layout and spacing](#layout-and-spacing)
3. [Color and dark mode](#color-and-dark-mode)
4. [Typography](#typography)
5. [Icons and images](#icons-and-images)
6. [Component guide](#component-guide)
7. [Windows, menus and navigation](#windows-menus-and-navigation)
8. [Accessibility checklist](#accessibility-checklist)
9. [Motion](#motion)
10. [Localization](#localization)
11. [Design acceptance checklist](#design-acceptance-checklist)
12. [References](#references)

## Principles

- **Native first.** Use MyGo's widgets and the theme as they are. A control that looks and behaves like the platform's
  is learned already. Style an element yourself only when no widget does the job, and build it on the
  [custom widget](https://github.com/egoist/mygo/blob/main/docs/ui/custom-widgets.md) bases so focus, keyboard and
  accessibility stay intact.
- **Consistent across platforms, respectful of each.** One view serves macOS, Windows and Linux. Follow each platform's
  conventions where MyGo exposes them: menu roles, the accent color, the system font, shortcuts that use
  `CmdOrCtrl`. Do not add chrome that imitates one platform on the others.
- **Accessible by default.** Every element can be reached with the keyboard, named for a screen reader, read in both
  appearances, and still works at larger text sizes. See the [checklist](#accessibility-checklist).
- **Restrained motion.** Motion explains a change; it never decorates. Honor the desktop's reduce-motion setting.
- **Meaning is never carried by color alone.** Pair color with text, a symbol or a shape.
- **The UI thread draws.** A frame is built from in-memory state. No disk, network or other blocking work in a view;
  start it in a goroutine and change the state afterwards (see
  [Views](https://github.com/egoist/mygo/blob/main/docs/ui/views.md)).

## Layout and spacing

Layout uses flexbox in device-independent pixels (DIPs); see
[Layout](https://github.com/egoist/mygo/blob/main/docs/ui/layout.md).

- **One spacing unit.** The theme's `Spacing` (4 DIPs by default; 3 is compact, 5 roomy) is the unit of every widget's
  padding and gap. Size your own elements with `t.Space(n)` so they follow it. Do not write raw pixel numbers for
  spacing.
- **Scale.** Use whole multiples of the unit: 1 (4) between a label and its control, 2 (8) between related controls,
  4 (16) between groups, 6 (24) for the window's outer padding. Larger gaps need a reason, for example a section
  break.
- **Structure from containers.** `Column` and `Row` with `Gap` and `Padding`; `Grow(1)` and `Spacer` for free space;
  `Grid` for forms and aligned tables of controls. Prefer `Gap` to margins on individual children.
- **Sizes are bounds.** Give windows a minimum size and let content reflow; do not fix a width a translation can
  overflow. Use `MinWidth`, `MaxWidth` and `Grow` instead of fixed widths, except for square symbol buttons.
- **Align to the baseline of the layout.** Left-align text and labels (right-aligned in right-to-left scripts if you
  add them); center only isolated focal content, as the fixture's counter.
- **Scrolling.** Content that can exceed the window goes in a
  [scroll view](https://github.com/egoist/mygo/blob/main/docs/ui/scroll.md) or a
  [list](https://github.com/egoist/mygo/blob/main/docs/ui/list.md) that builds only the rows in view.
- **Fixture.** Window 480×320, minimum 360×280; padding `Space(6)`; vertical gap `Space(4)`; button gap `Space(2)`;
  symbol buttons `Space(11)` wide. The reset button grows to fit its localized label.

## Color and dark mode

Colors come from the theme, `c.Theme()`: it is the light or dark theme, switches when the system appearance changes,
and carries the user's accent color and contrast settings. See
[Styling and themes](https://github.com/egoist/mygo/blob/main/docs/ui/styling.md).

- **Always use theme roles, never literals.** Hard-coded colors do not follow dark mode, accent or high contrast.

  | Role | Use |
  |---|---|
  | `Background` | window and page fill |
  | `Surface`, `SurfaceHover`, `SurfacePressed` | faces of controls and cards, and their states |
  | `Border` | outlines and dividers |
  | `Text`, `TextMuted` | primary text; secondary text, hints and placeholders |
  | `Accent`, `AccentHover`, `AccentPressed`, `AccentText` | primary action, selection and checked controls; text on the accent |
  | `Danger`, `Warning`, `Success` | destructive, cautionary and positive status (always with text or a symbol) |
  | `Selection`, `Focus` | selected text; the keyboard focus ring |
  | `Inverse`, `InverseText` | tooltips and toasts |

- **Appearance.** Do not implement your own dark mode switch; the theme follows the system. If a screen draws custom
  elements, read `c.Theme().Dark` or, better, only theme colors. For derived colors use `Mix` and `Alpha` on theme
  colors rather than new constants.
- **Accent.** One primary action per screen uses `PrimaryButton`. Do not recolor the accent unless the product has a
  brand color; if it does, set `Accent` in one place on a copy of the theme and verify contrast in both appearances.
- **Contrast.** Text and meaningful graphics should meet WCAG 2.1 AA: 4.5:1 for body text, 3:1 for large text and
  control boundaries. Test with the desktop's high contrast setting on (`c.Preferences().HighContrast`).
- **Status.** Color supplements a message; the message states the status in words.
- **Mockups.** Colors in `design/screens/` are approximations of the default theme; device acceptance verifies the
  real result.

## Typography

- **System font.** Leave `Font` empty so text uses the platform's UI font. Default text size is 13 on macOS and 14
  elsewhere, and scales with the desktop's text size (`Preferences().TextScale`) when you rely on the theme. See
  [Text](https://github.com/egoist/mygo/blob/main/docs/ui/text.md).
- **Size relative to the theme.** Use `t.Rem(n)` for sizes (`n` times the theme font size) rather than fixed numbers,
  so custom text follows the user's text scale. Fixture: title 1.8 rem bold, count 3.6 rem bold, hint 0.9 rem in
  `TextMuted`. Widget text uses the theme size.
- **Hierarchy with few steps.** Body, secondary (`TextMuted`, about 0.9 rem), section heading (bold) and at most one
  display size. Weight and color before size.
- **Headings are real headings.** Give the title of a screen or section `Role(ui.RoleHeading)` and a `Level` so
  assistive technology can navigate by them.
- **Do not truncate silently.** Prefer wrapping; where a single line is needed (`SingleLine`), ensure the full text is
  available in a tooltip or elsewhere.
- **Numbers.** Show numbers in the user's locale when they are data, not identifiers.

## Icons and images

- **Icons are SVG** shown with `ui.Icon`, which takes the text color and the font size: an icon follows theme colors
  and the text size automatically. Any set that uses plain SVG (Lucide, Heroicons, Tabler, Material Symbols) works.
  Embed them with `go:embed` and parse once at package level. See
  [Icon](https://github.com/egoist/mygo/blob/main/docs/ui/icon.md).
- **An icon needs a name when it is alone.** Icons are decoration for assistive technology unless given a `Label`.
  A button that shows only an icon gets a `Label`; an icon next to a visible text label needs none.
- **Icon before label** in buttons, one icon style per product, sized with `FontSize`.
- **Bitmaps and SVG in their own colors** use [Image](https://github.com/egoist/mygo/blob/main/docs/ui/image.md);
  people use [Avatar](https://github.com/egoist/mygo/blob/main/docs/ui/avatar.md).
- **Fixture.** The counter uses the text symbols `+` and `−` with localized accessible labels. Replace the product
  icon (in `mygo.json` and `resources/`) before shipping.

## Component guide

Pick the widget by the job. Each name links to the upstream page, which also says what assistive technology sees of
the widget. The complete list is the
[UI index](https://github.com/egoist/mygo/blob/main/docs/ui/README.md).

### Actions

| Need | Use |
|---|---|
| The main action of a screen, once | [Button](https://github.com/egoist/mygo/blob/main/docs/ui/button.md) (`PrimaryButton`) |
| Other actions | [Button](https://github.com/egoist/mygo/blob/main/docs/ui/button.md) |
| Navigate to a URL or page | [Link](https://github.com/egoist/mygo/blob/main/docs/ui/link.md) |
| Several related actions in one place | [Menu button](https://github.com/egoist/mygo/blob/main/docs/ui/menu-button.md) |
| Actions on a specific item, on right click | [Context menu](https://github.com/egoist/mygo/blob/main/docs/ui/context-menu.md) |
| An on/off command that stays pressed (bold) | [Toggle](https://github.com/egoist/mygo/blob/main/docs/ui/toggle.md) |
| Choose one of a few views or modes | [Segmented control](https://github.com/egoist/mygo/blob/main/docs/ui/segmented.md) |
| Window-level commands | [Toolbar](https://github.com/egoist/mygo/blob/main/docs/ui/toolbar.md) |

### Choices

| Need | Use |
|---|---|
| A setting applied immediately | [Switch](https://github.com/egoist/mygo/blob/main/docs/ui/switch.md) |
| A yes/no value submitted with a form, or several independent options | [Checkbox](https://github.com/egoist/mygo/blob/main/docs/ui/checkbox.md) |
| One of two to five visible options | [Radio](https://github.com/egoist/mygo/blob/main/docs/ui/radio.md) |
| One of many options | [Select](https://github.com/egoist/mygo/blob/main/docs/ui/select.md); with typing to filter, [Combobox](https://github.com/egoist/mygo/blob/main/docs/ui/combobox.md) |
| A value in a range | [Slider](https://github.com/egoist/mygo/blob/main/docs/ui/slider.md); an exact number, [Number input](https://github.com/egoist/mygo/blob/main/docs/ui/number-input.md) or [Stepper](https://github.com/egoist/mygo/blob/main/docs/ui/stepper.md) |
| A low and a high value | [Range slider](https://github.com/egoist/mygo/blob/main/docs/ui/range-slider.md) |
| A rating | [Rating](https://github.com/egoist/mygo/blob/main/docs/ui/rating.md) |

### Text, dates and colors

| Need | Use |
|---|---|
| Free text, one or many lines | [Text input](https://github.com/egoist/mygo/blob/main/docs/ui/text-input.md) |
| Searching | [Search field](https://github.com/egoist/mygo/blob/main/docs/ui/search-field.md), or [Find bar](https://github.com/egoist/mygo/blob/main/docs/ui/find-bar.md) for text in a document |
| Text with suggestions | [Autocomplete](https://github.com/egoist/mygo/blob/main/docs/ui/autocomplete.md) |
| Tags or recipients | [Token field](https://github.com/egoist/mygo/blob/main/docs/ui/token-field.md) |
| Rename in place | [Editable text](https://github.com/egoist/mygo/blob/main/docs/ui/editable-text.md) |
| A date or a time | [Calendar](https://github.com/egoist/mygo/blob/main/docs/ui/calendar.md), [Date input](https://github.com/egoist/mygo/blob/main/docs/ui/date-input.md), [Time input](https://github.com/egoist/mygo/blob/main/docs/ui/time-input.md) |
| A color | [Color picker](https://github.com/egoist/mygo/blob/main/docs/ui/color-picker.md) |
| Labeled controls with help and errors | [Form](https://github.com/egoist/mygo/blob/main/docs/ui/form.md) |

### Collections

| Need | Use |
|---|---|
| Many rows of one kind | [List](https://github.com/egoist/mygo/blob/main/docs/ui/list.md) |
| Rows with sortable, resizable columns | [Table](https://github.com/egoist/mygo/blob/main/docs/ui/table.md) |
| Hierarchy | [Tree](https://github.com/egoist/mygo/blob/main/docs/ui/tree.md), or [Outline](https://github.com/egoist/mygo/blob/main/docs/ui/outline.md) when large |
| Thumbnails | [Grid view](https://github.com/egoist/mygo/blob/main/docs/ui/grid-view.md) |

### Containers and navigation

| Need | Use |
|---|---|
| Scrolling content | [Scroll view](https://github.com/egoist/mygo/blob/main/docs/ui/scroll.md) |
| Columns and rows of controls | [Grid](https://github.com/egoist/mygo/blob/main/docs/ui/grid.md) |
| Two resizable panes | [Split view](https://github.com/egoist/mygo/blob/main/docs/ui/split.md) |
| Optional detail | [Collapsible](https://github.com/egoist/mygo/blob/main/docs/ui/collapsible.md), [Accordion](https://github.com/egoist/mygo/blob/main/docs/ui/accordion.md) |
| Top-level sections of an app | [Sidebar](https://github.com/egoist/mygo/blob/main/docs/ui/sidebar.md) |
| A few peer pages inside a screen | [Tabs](https://github.com/egoist/mygo/blob/main/docs/ui/tabs.md) |
| Pages with a history | [Router](https://github.com/egoist/mygo/blob/main/docs/ui/navigation.md), with [Back and forward buttons](https://github.com/egoist/mygo/blob/main/docs/ui/history-buttons.md) |
| Where the user is in a hierarchy | [Breadcrumbs](https://github.com/egoist/mygo/blob/main/docs/ui/breadcrumbs.md) |

### Dialogs, messages and status

| Need | Use |
|---|---|
| A task that needs the user's full attention | [Dialog](https://github.com/egoist/mygo/blob/main/docs/ui/dialog.md) |
| Confirm something important or destructive | [Alert dialog](https://github.com/egoist/mygo/blob/main/docs/ui/alert-dialog.md); for system file and message dialogs, `mygo.Dialog` ([desktop APIs](https://github.com/egoist/mygo/blob/main/docs/native.md)) |
| A small panel tied to an element | [Popover](https://github.com/egoist/mygo/blob/main/docs/ui/popover.md) |
| A short label or hint for a control | [Tooltip](https://github.com/egoist/mygo/blob/main/docs/ui/tooltip.md) (never the only place for essential information) |
| Feedback that needs no decision | [Toast](https://github.com/egoist/mygo/blob/main/docs/ui/toast.md) |
| Known progress / unknown duration | [Progress bar](https://github.com/egoist/mygo/blob/main/docs/ui/progress.md) / [Spinner](https://github.com/egoist/mygo/blob/main/docs/ui/spinner.md) |
| A value against thresholds | [Meter](https://github.com/egoist/mygo/blob/main/docs/ui/meter.md) |
| A count or short status | [Badge](https://github.com/egoist/mygo/blob/main/docs/ui/badge.md) |

Overlays share focus and Escape behavior; see
[Overlays](https://github.com/egoist/mygo/blob/main/docs/ui/overlays.md). Rules of thumb:

- Prefer undo over confirmation. Confirm only what cannot be undone, with a button named for the action ("Delete"),
  not "OK", and Cancel as the Escape action.
- Do not stack dialogs. Use a toast for news that needs no answer.
- Errors say what happened and what to do, next to the control that caused them (`Error`, or a
  [form](https://github.com/egoist/mygo/blob/main/docs/ui/form.md) field).

## Windows, menus and navigation

- **Windows.** One main window; set `Title`, `Width`, `Height`, and `MinWidth`/`MinHeight` so content never clips.
  `StateKey` remembers size and position between runs. Windows with native UI need no webview. See
  [Windows with native UI](https://github.com/egoist/mygo/blob/main/docs/ui/windows.md) and the
  [window options](https://github.com/egoist/mygo/blob/main/docs/windows.md).
- **Title bar.** Keep the system title bar unless the product needs more. A hidden title bar
  (`TitleBarHidden`) makes the view responsible for the room the window controls take (`c.TitleBar()`) and for a
  draggable area (`DragWindow`).
- **Vibrancy and materials.** macOS vibrancy shows where the view draws no background; use it for sidebars only, over
  opaque content. The fixture uses an opaque theme surface and no custom glass.
- **Menus.** The macOS menu bar belongs to the app; keep the app menu and edit menu (`RoleAppMenu`, `RoleEditMenu`) so
  Cmd+Q, copy and paste work. Use roles (`RoleAbout`, `RoleQuit`, `RoleWindowMenu`) for standard items: they carry the
  right label and shortcut, and are omitted where a platform has no such item. Give custom items an accelerator with
  `CmdOrCtrl`. Every command reachable by a toolbar button should also be in a menu. See
  [Menus](https://github.com/egoist/mygo/blob/main/docs/menus.md).
- **Navigation.** Choose the lightest structure that fits: a single screen; [tabs](https://github.com/egoist/mygo/blob/main/docs/ui/tabs.md)
  for a few peer views; a [sidebar](https://github.com/egoist/mygo/blob/main/docs/ui/sidebar.md) with a
  [router](https://github.com/egoist/mygo/blob/main/docs/ui/navigation.md) for several top-level sections. A router
  gives back/forward keys, state restored per page and focus handling for free. Give every page a `Title`.
- **Toolbar.** Frequent window-level commands, in order of importance; controls that do not fit overflow into a menu.
- **Notifications.** Use system notifications only for events the user would want when the app is in the background.

## Accessibility checklist

MyGo exposes native UI to VoiceOver, Narrator, NVDA and Orca; see
[Accessibility](https://github.com/egoist/mygo/blob/main/docs/ui/accessibility.md).

- [ ] Every interactive element has an accessible name: its text, or `Label` when it shows only an icon or a drawing.
- [ ] `Description` carries help text; `Error` marks invalid values.
- [ ] Custom elements that act as widgets set `Role`, and the states they show (`Checked`, `Expanded`, `Range`).
- [ ] Section and screen titles are headings with a `Level`.
- [ ] Changes that do not move the focus (a result count, a saved file, a changing value) call `c.Announce(text)`.
      Toasts and router page titles announce themselves.
- [ ] The whole UI works with the keyboard: Tab order follows reading order, there is a visible focus ring (do not
      remove it), shortcuts exist for frequent actions, Escape closes overlays.
- [ ] Text uses theme sizes (`Rem`) and scales; layouts reflow at larger text and in the longest translation.
- [ ] Colors are theme roles; contrast holds in both appearances and with high contrast on.
- [ ] Nothing depends on color, sound or motion alone.
- [ ] Pointer targets are at least about 24×24 DIPs, and 32 or more for primary controls.
- [ ] `ui.NewTester` tests click controls by their accessible names, so a missing name fails the test.

A headless test does not prove operating-system accessibility. Check with a real screen reader on each target before
release.

## Motion

Motion explains what changed and where it went; it does not decorate. See
[Transitions](https://github.com/egoist/mygo/blob/main/docs/ui/transitions.md) and
[Drawing and animation](https://github.com/egoist/mygo/blob/main/docs/ui/drawing.md).

- **Default is none.** State changes are immediate unless a transition clarifies a change in layout.
- **Short and eased out.** Element transitions default to 200 ms ease-out; hover color changes use about 120 ms. Use
  nothing longer than 300 ms for interface feedback.
- **Use the built-ins.** `Transition` for elements that move, resize, appear or leave; the router's page transitions
  for navigation; `Animate` for values. Avoid frame-by-frame custom animation.
- **Honor reduced motion.** `Animate` and element and page transitions already jump to the target when the desktop
  asks for less motion (`c.Preferences().ReduceMotion`). Any motion you compute yourself must read the preference.
  Spinners may keep turning: they show that work is going on.
- **Never animate to hide latency**, and do not loop decoration.
- **Fixture.** None; the count changes at once.

## Localization

- English is the source language; every user-visible string is in the embedded catalog `copy.json` next to the
  screen, keyed by language: `en`, `zh-Hans`, `zh-Hant`, `ja`, `ko`, `fr`, `de`, `es`, `pt-BR`.
- `New(locale)` maps the system locale to a catalog (`zh-TW`, `zh-HK` and `zh-Hant` to Traditional Chinese, other
  `zh` to Simplified, `pt` to Brazilian Portuguese) and falls back to English.
- Every key has all nine translations, and a test fails on a missing or untranslated entry. Accessible names are copy
  too: translate `Label` and `Description`.
- Write short action labels in the imperative ("Increment", "Reset"); sentence case; no trailing period on labels,
  full stop on sentences. Avoid concatenating sentence fragments, since word order differs; use full-sentence
  strings with placeholders.
- Layouts must tolerate text 30–50% longer than English. Do not fix widths of text controls.
- Format dates, numbers and plurals for the locale. Plural rules differ; provide separate strings where it matters.

## Design acceptance checklist

- [ ] All three counter states (zero, positive, negative), nine languages, light and dark, both window sizes checked.
- [ ] Keyboard-only run-through, and a screen reader pass on each target platform.
- [ ] High contrast and larger text size checked.
- [ ] Product screens are explicitly signed off and accepted by the maintainer.

## References

This design language draws on the UI documentation of MyGo (MIT License, Copyright (c) egoist):
<https://github.com/egoist/mygo/tree/main/docs/ui>, together with `docs/native.md`, `docs/menus.md` and
`docs/windows.md`. The text here is a summary in our own words; the upstream pages are the source for APIs and
behavior. The template pins MyGo v0.2.16; upstream `main` may describe newer APIs. See also
[THIRD_PARTY.md](../THIRD_PARTY.md).
