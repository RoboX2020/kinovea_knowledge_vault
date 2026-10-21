---
id: "5b"
title: "Spatial calibration"
aliases: ["Spatial calibration"]
tags: [kinovea, type/structure, kinovea/measurement]
up: "[[5 Measurement]]"
source: official-manual
---

# Spatial calibration

In order to use Kinovea to make measurements on the video, it is necessary to calibrate the transformation of pixels in the image into real world units. Kinovea supports two calibration mechanisms: calibration by line and calibration by plane.

All measurements in Kinovea must sit on a 2D plane. If the motion you want to study is on a plane parallel to the image plane (orthogonal to the camera optical axis), you may use calibration by line. Otherwise, if you are measuring points on the ground, for example, you should use the calibration by plane. If the motion is happening in arbitrary 3D space you cannot measure it in Kinovea.

## Notes in this chapter

- [[5b1 Line calibration]] — Line calibration is possible when the motion is sitting on a 2D plane parallel to the camera plane.
- [[5b2 Plane calibration]] — Plane calibration is possible when the motion is sitting on an arbitrary 2D plane visible in the video.

---
⬆ [[5 Measurement]] · ⬅ [[5a Measurement]] · ➡ [[5c Lens distortion calibration]]
