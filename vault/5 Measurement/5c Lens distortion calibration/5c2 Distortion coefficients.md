---
id: "5c2"
title: "Distortion coefficients"
aliases: ["Distortion coefficients"]
tags: [kinovea, type/permanent, kinovea/measurement]
up: "[[5c Lens distortion calibration]]"
source: official-manual
---

# Distortion coefficients

The description of the lens distortion is done in the lens calibration dialog in the menu **Tools ‣ Camera calibration**.

There are multiple approaches to finding coefficients that best match a particular camera lens and camera mode, they are described below.

All the approaches involve filming a highly structured pattern in order to facilitate the distortion estimation, whether it is done visually or programmatically. This pattern can be a chess board, a brick wall, or any structured image displayed on a flat screen.

The following parameters are used during calibration:

- **fx**, **fy**: focal length in pixels.

- **cx**, **cy**: pixel coordinates of the optical center.

- **k1**, **k2**, **k3**: radial distortion coefficients.

- **p1**, **p2**: tangential distortion coefficients.

---
⬆ [[5c Lens distortion calibration]] · ⬅ [[5c1 Introduction]] · ➡ [[5c3 Visual estimation]]
