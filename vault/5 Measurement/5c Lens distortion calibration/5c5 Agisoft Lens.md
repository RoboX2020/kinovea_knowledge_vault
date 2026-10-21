---
id: "5c5"
title: "Agisoft Lens"
aliases: ["Agisoft Lens"]
tags: [kinovea, type/permanent, kinovea/measurement]
up: "[[5c Lens distortion calibration]]"
source: official-manual
---

# Agisoft Lens

Agisoft Lens is an automatic lens calibration software.

![[distortionagisoft.png]]

> [!note]
> Agisoft Lens as a free, standalone desktop software is no longer published by Agisoft.

To use Agisoft Lens to calibrate the lens distortion follow these steps:

- Open Agisoft Lens and display the chessboard using the **Show chessboard** button.

- Film the chessboard displayed from up close in such a way that only parts of the chessboard are visible, not the background of the monitor.

- Open the video in Kinovea and export at least five images to separate files.

- In Agisoft Lens import the images using the **Add photos** button.

- Start calibration by using the **Calibrate** button, selecting the following options:

  - Fit cx, cy;

  - Fit k1, k2, k3;

  - Fit aspect;

  - Fit p1, p2.

- Use Save calibration to save an XML file of the solved parameters.

- In Kinovea open the lens calibration dialog and do **File ‣ Import ‣ Agisoft Lens**.

This will convert and fill the distortion parameters.

---
⬆ [[5c Lens distortion calibration]] · ⬅ [[5c4 Distortion grid]] · ➡ [[5c6 Exporting and importing distortion parameters]]
