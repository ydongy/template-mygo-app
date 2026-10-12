# Template design language

## Principles

Native controls and theme defaults. Draw from UI-thread state; no work that blocks a frame.
The counter is a neutral fixture; replace it with your own design.

## Core symbol

The numeric count is the only focal element. Meaning is expressed in text, never color alone.

## Color

Use MyGo theme colors and TextMuted for the hint. Follow system light/dark and accent.
Mockup colors are approximations; device acceptance verifies the real result.

## Typography

System font. Title 24, bold; count 48, bold; hint 12. Controls use MyGo defaults.

## Layout and spacing

Window 480×320, minimum 360×280. Outer padding 24; vertical gap 16; button gap 8;
symbol button width 44. The reset button fits its localized label.

## Materials

Opaque system-themed surface. No custom glass or layered translucent panels.

## Icons

Text symbols + and − have localized accessible labels. Replace the product icon before shipping.

## Motion

No custom animation. State changes are immediate.

## Signature moments

None.

## Copy tone

Short action labels. English is the source; every UI label has all nine translations.

## Accessibility

Use named buttons and standard focus behavior. Verify contrast, resize, keyboard and screen readers
on real target devices. Passing a headless tester does not prove operating-system accessibility.

## Design acceptance checklist

- [ ] All three counter states, nine languages, light/dark and both window sizes checked.
- [ ] Product screens are explicitly signed off and accepted by the maintainer.
