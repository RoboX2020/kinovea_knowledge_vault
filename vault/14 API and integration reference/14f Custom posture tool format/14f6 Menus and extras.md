---
id: "14f6"
title: "Menus and extras"
aliases: ["Menus and extras"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14f Custom posture tool format]]"
source: kinovea-source-code
---

# Menus and extras

- `optionGroup` on any element links it to a context-menu toggle; the element is drawn only when the option is on. Combine several with `|` (`optionGroup="a|b"`): **all** must be on (AND logic).

- Options are created **automatically** from every `optionGroup` value, labelled with that value and **off by default**. That’s how *Human model* gets its “Display knee angles” toggles without declaring anything.

- `Options/Option key label default hidden` declares an option explicitly, to set a friendlier `label`, make it `default="true"`, or keep it out of the menu with `hidden="true"` (used by the OpenPose model).

- `Capabilities flipHorizontal flipVertical` — adds Flip menu items. Must be an empty element.

- `TrackingParameters` — per-tool tracking parameter overrides.

---
⬆ [[14f Custom posture tool format]] · ⬅ [[14f5 Variables section]] · ➡ [[14f7 Tips]]
