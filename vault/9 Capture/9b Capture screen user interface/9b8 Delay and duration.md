---
id: "9b8"
title: "Delay and duration"
aliases: ["Delay and duration"]
tags: [kinovea, type/permanent, kinovea/capture]
up: "[[9b Capture screen user interface]]"
source: official-manual
---

# Delay and duration

![[capture-delay-controls.png]]

The delay numerical field and slider let you adjust the amount of delay, in seconds, of the camera stream.

The delay setting can be ignored for the viewport image by using the ![[live-live.png]] Live view button in the capture controls. In this case the delay is still taken into account when recording if the recording mode is set to Delayed or Retroactive.

The maximum amount of delay depends on the camera configuration — hardware compression, image format, image size, frame rate — and the memory allocated in the delay cache under **Options ‣ Preferences ‣ Capture ‣ Memory**.

The duration numerical field let you set a maximum duration for the recording. This is the total duration of the resulting file.

> [!note]
> If delay is set to 2 seconds and maximum duration is set to 3 seconds, the resulting file will be 3 seconds long and contain 2 seconds of action *before* the recording button was pressed or triggered, and 1 second of action *after* the recording button was pressed or triggered.

---
⬆ [[9b Capture screen user interface]] · ⬅ [[9b7 Capture controls]] · ➡ [[9b9 Output folder and file name]]
