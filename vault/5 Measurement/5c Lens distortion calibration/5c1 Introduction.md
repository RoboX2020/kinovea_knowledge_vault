---
id: "5c1"
title: "Introduction"
aliases: ["Introduction"]
tags: [kinovea, type/permanent, kinovea/measurement]
up: "[[5c Lens distortion calibration]]"
source: official-manual
---

# Introduction

When using cameras with significant distortion is it important to calibrate it in Kinovea before making measurements. The lens distortion calibration rectifies the coordinates before they are passed to the spatial calibration.

![[distorted-coordinatesystem.png]]

Barrel distortion exposed by a GoPro action camera and the default coordinate system after lens distortion calibration.

Lens calibration is compatible with both line calibration and plane calibration. The coordinate system, lines and grid objects are drawn distorted to follow the distortion. The images themselves are not rectified.

![[distorted-coordinatesystem-plane.png]]

---
⬆ [[5c Lens distortion calibration]] · ➡ [[5c2 Distortion coefficients]]
