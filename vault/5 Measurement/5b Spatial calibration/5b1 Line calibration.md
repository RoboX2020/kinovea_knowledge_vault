---
id: "5b1"
title: "Line calibration"
aliases: ["Line calibration"]
tags: [kinovea, type/permanent, kinovea/measurement]
up: "[[5b Spatial calibration]]"
source: official-manual
---

# Line calibration

Line calibration is possible when the motion is sitting on a 2D plane parallel to the camera plane.

![[planeofmotion.png]]

To perform line calibration follow these steps:

- Have an object of known length visible in the video.

- Add a line object and place it on top of the object of known length.

- Right click the line and select the **Calibrate** menu.

- Enter the real-world length of the object.

![[calibrationline.png]]

> [!note]
> Modifying the calibration line after calibration already took place will update the calibration to use the new pixel length of the line and keep the real-world length as configured.

---
⬆ [[5b Spatial calibration]] · ➡ [[5b2 Plane calibration]]
