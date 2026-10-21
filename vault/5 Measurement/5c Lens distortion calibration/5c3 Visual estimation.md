---
id: "5c3"
title: "Visual estimation"
aliases: ["Visual estimation"]
tags: [kinovea, type/permanent, kinovea/measurement]
up: "[[5c Lens distortion calibration]]"
source: official-manual
---

# Visual estimation

In this approach the distortion is estimated visually by directly changing the distortion coefficients and trying to align the grid on the image. It is the least accurate approach but can still provide decent results.

![[distortion.png]]

Follow these steps:

- Film the pattern straight on.

- Load the video and open the lens calibration dialog.

- Tweak k1 and k2 distortion coefficients to match the distorted grid image.

  - k1 is the distortion of the first order and should be used as a starting point to get the grid to align as best as possible in the central region of the image.

  - k2 can be used to counteract the main distortion at the periphery of the image.

- You can play with the cx, cy, p1, p2 parameters as well to adjust the grid to the image.

---
⬆ [[5c Lens distortion calibration]] · ⬅ [[5c2 Distortion coefficients]] · ➡ [[5c4 Distortion grid]]
