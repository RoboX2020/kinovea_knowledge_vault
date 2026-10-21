---
id: "5c4"
title: "Distortion grid"
aliases: ["Distortion grid"]
tags: [kinovea, type/permanent, kinovea/measurement]
up: "[[5c Lens distortion calibration]]"
source: official-manual
---

# Distortion grid

In this approach the distortion is estimated programmatically by Kinovea from a set of distortion grid objects manually placed over images of the video.

![[distortiongriddemo.png]]

Follow these steps:

- Film a chess board or structured pattern from various angles.

- Select some images (for example five) and add a Distortion grid object.

![[distortiongridbutton.png]]

- Map each point of each grid onto corners on the filmed pattern.

![[distortiongridzoom.png]]

- Open the lens calibration dialog and click the **Calibrate camera** button in the lower left.

This will compute and fill the distortion parameters.

---
⬆ [[5c Lens distortion calibration]] · ⬅ [[5c3 Visual estimation]] · ➡ [[5c5 Agisoft Lens]]
