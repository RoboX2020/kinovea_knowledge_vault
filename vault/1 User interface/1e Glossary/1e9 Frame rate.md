---
id: "1e9"
title: "Frame rate"
aliases: ["Frame rate"]
tags: [kinovea, type/permanent, kinovea/user-interface]
up: "[[1e Glossary]]"
source: official-manual
---

# Frame rate

Kinovea deals with multiple frame rates:

- camera frame rate: frame rate *configured* in the camera (ex: 200 fps)

- capture frame rate: frame rate actually *captured* by the camera (ex: 195 fps)

- capture screen “display frame rate”: refresh rate of the capture screen (ex: 10 fps)

- video frame rate: nominal playback rate stored as a metadata in the video file (ex: 30 fps)

- playback frame rate: frame rate at which the video is being played back.

When capturing from a high speed camera (capture frame rate \> 150 fps) it is customary to set the video frame rate to a lower value (ex: 30 fps) to allow for smooth playback.

Knowing the capture frame rate is important for time-based measurements such as speed and acceleration.

---
⬆ [[1e Glossary]] · ⬅ [[1e8 Drawing, Drawing tools]] · ➡ [[1e10 Intra-only, Intra-frame, All-i, All-Intra]]
