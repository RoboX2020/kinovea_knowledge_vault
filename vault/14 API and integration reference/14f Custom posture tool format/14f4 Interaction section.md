---
id: "14f4"
title: "Interaction section"
aliases: ["Interaction section"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14f Custom posture tool format]]"
source: kinovea-source-code
---

# Interaction section

`Handles/Handle` makes something draggable. Attributes: `type` (`Point` \| `Segment` \| `Circle` \| `Ellipse`), `reference` (index of the point/segment/circle), `trackable` (included in tracking), `color`, `name`, `optionGroup`.

A handle may contain one **constraint** (where it is allowed to go) and **impacts** (what else moves when it moves).

`Constraint` takes `type` and an optional `optionGroup`, and a child element carrying that type’s parameters:

| Constraint type                     | Parameters / meaning                                                         |
|-------------------------------------|------------------------------------------------------------------------------|
| `None`                              | Free movement.                                                               |
| `LineSlide`                         | `point1`, `point2`, `position` — slide along the line through two points.    |
| `VerticalSlide` / `HorizontalSlide` | Move only vertically / horizontally.                                         |
| `DistanceToPoint`                   | `point` — keep a fixed distance (move on a circle).                          |
| `RotationSteps`                     | `origin`, `leg1`, `step` (degrees), `keepDistance` — snap rotation to steps. |
| `PerpendicularSlide`                | `origin`, `leg1` — slide perpendicular to a leg.                             |
| `ParallelSlide`                     | `a`, `b`, `c` — keep parallel to a reference segment.                        |
| `LockedInPlace`                     | Cannot be moved.                                                             |

`Impacts` (or `Impact`) contains any of:

| Impact element                      | Parameters / meaning                                                                                                                           |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `Align`                             | `point1`, `point2`, `pointToAlign` — keep a point on a line.                                                                                   |
| `VerticalAlign` / `HorizontalAlign` | `point` — keep a point vertically / horizontally aligned with the handle.                                                                      |
| `Pivot`                             | `pivot`, `impacted` — rotate other points around a pivot.                                                                                      |
| `KeepAngle`                         | `origin`, `leg1`, `leg2` — preserve an angle.                                                                                                  |
| `HorizontalSymmetry`                | `axis`, `impacting`, `impacted` — mirror a point across an axis.                                                                               |
| `SegmentCenter`                     | `point1`, `point2`, `pointToMove` — keep a point at a segment’s midpoint.                                                                      |
| `PerdpendicularAlign`               | `origin`, `leg1`, `pointToMove`. **Note the misspelling**: the parser expects `PerdpendicularAlign`. The correct spelling is silently ignored. |
| `ParallelAlign`                     | `a`, `b`, `c`, `pointToMove`.                                                                                                                  |

`HitZone/Polygon points="2;11;15;6"` defines an area; dragging inside it moves the whole drawing.

---
⬆ [[14f Custom posture tool format]] · ⬅ [[14f3 Data section]] · ➡ [[14f5 Variables section]]
