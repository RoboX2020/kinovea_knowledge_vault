---
id: "5b2"
title: "Plane calibration"
aliases: ["Plane calibration"]
tags: [kinovea, type/permanent, kinovea/measurement]
up: "[[5b Spatial calibration]]"
source: official-manual
---

# Plane calibration

Plane calibration is possible when the motion is sitting on an arbitrary 2D plane visible in the video.

To perform plane calibration follow these steps:

- Have a rectangle of known dimensions visible in the video.

- Add a perspective grid object and move its corners to match the rectangle.

- Right click a corner and select the **Calibrate** menu.

- Enter the real-world width and height of the rectangle.

![[calibrationplane.png]]

> [!note]
> Modifying the calibration plane after calibration already took place will update the calibration to use the new pixel dimensions of the plane while keeping the real-world dimension as configured.

---
⬆ [[5b Spatial calibration]] · ⬅ [[5b1 Line calibration]]
