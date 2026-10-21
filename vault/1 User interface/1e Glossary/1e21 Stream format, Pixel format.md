---
id: "1e21"
title: "Stream format, Pixel format"
aliases: ["Stream format, Pixel format"]
tags: [kinovea, type/permanent, kinovea/user-interface]
up: "[[1e Glossary]]"
source: official-manual
---

# Stream format, Pixel format

The stream format describes the content of the video frames as delivered by the camera. Camera vendors tend to use different names for the same thing but in the end there are only a few formats we are interested in:

- MJPEG, JPEG, etc. Good for frame by frame navigation, low bandwidth and low CPU usage.

- RGB, RGB8, RGB24, RGB32. Avoid this if possible. High bandwidth and high CPU.

- BayerRG8, BayerBG8, etc. Use this if available and check “Enable software demosaicing”.

- Mono8, Y800, for monochrome cameras.

---
⬆ [[1e Glossary]] · ⬅ [[1e20 Stabilization, Image stabilization]] · ➡ [[1e22 Synchronization]]
