---
id: "14f5"
title: "Variables section"
aliases: ["Variables section"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14f Custom posture tool format]]"
source: kinovea-source-code
---

# Variables section

- `Distances/Distance point1 point2` — display a measured distance; `symbol`, `color`, `name`, `optionGroup`.

- `Positions/Position point` — display coordinates of a point; `symbol`, `color`, `optionGroup`.

- `ComputedPoints/ComputedPoint` — a weighted point, e.g. center of mass. Nest `ComputedPoint` (with `weight`) and `ReferencePoint ref="<index>" weight="…"` arbitrarily deep; `name`, `color`, `symbol`, `displayCoordinates`, `optionGroup`. Computed points are referenced elsewhere with a `$` prefix (`point="$0"` = first computed point). See *10 - Human model.xml* for a full anthropometric center-of-mass model.

---
⬆ [[14f Custom posture tool format]] · ⬅ [[14f4 Interaction section]] · ➡ [[14f6 Menus and extras]]
