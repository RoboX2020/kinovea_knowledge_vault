---
id: "15a3"
title: "Tracked coordinate system"
aliases: ["Tracked coordinate system"]
tags: [kinovea, type/permanent, kinovea/legacy-documentation-obsolete, status/obsolete]
up: "[[15a Tracking distances and angles]]"
source: official-manual-legacy
---

# Tracked coordinate system

> [!warning] Obsolete
> From the *previous* Kinovea manual. These pages are no longer linked from the official docs and may describe older behavior; they are kept because the current manual's tracking chapters are still empty stubs.

The calibration mechanism uses a line object or a plane object to define a coordinate system and transform pixel coordinates into real world coordinates.

If the object defining the calibration is itself tracked, the calibration will be updated at every frame. This can be used to compensate a moving camera.

It is also possible to track the coordinate system origin while keeping the calibration static. This can be used to obtain coordinates of a point relatively to a moving reference.

> [!note]
> Tracking the calibration object and tracking the coordinate system are not compatible with each other. The tracked calibration object redefines the coordinate system.

---
⬆ [[15a Tracking distances and angles]] · ⬅ [[15a2 Tracking parameters]]
