---
id: "14f3"
title: "Data section"
aliases: ["Data section"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14f Custom posture tool format]]"
source: kinovea-source-code
---

# Data section

| Element                             | Attributes                                                                                                                                                                 |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Points/Point`                      | `value="x;y"` initial position; `name`, `color`. (Legacy 1.0 files use `InitialConfiguration/Point` with text content, and `PointCount`, which is ignored.)                |
| `Segments/Segment`                  | `point1`, `point2`; `name`, `style` (`Solid` \| `Dash`), `width`, `color`, `arrowBegin` / `arrowEnd` (`arrowStart` also accepted), `optionGroup`.                          |
| `Circles/Circle` (alias `Ellipses`) | `center` (point index), `radius`, `style`, `width`, `color`, `name`, `optionGroup`.                                                                                        |
| `Angles/Angle`                      | `origin`, `leg1`, `leg2`; `signed`, `ccw`, `supplementary`, `radius` (negative = inside), `textDistance`, `tenth` (one decimal), `symbol`, `color`, `name`, `optionGroup`. |
| `Polylines/Polyline`                | `points="0;1;2;3"`; `style`, `width`, `color`, `arrowBegin`/`arrowEnd`, `name`, `optionGroup`.                                                                             |

---
⬆ [[14f Custom posture tool format]] · ⬅ [[14f2 Real example- the shipped Goniometer]] · ➡ [[14f4 Interaction section]]
