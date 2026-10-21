---
id: "11a2"
title: "Applying delay"
aliases: ["Applying delay"]
tags: [kinovea, type/permanent, kinovea/delay-and-replay]
up: "[[11a Live delay]]"
source: official-manual
---

# Applying delay

To delay the display of the camera stream use the delay slider or the delay input box. The delay amount is in seconds.

![[delaycontrols.png]]

The maximum amount of delay depends on the camera configuration — hardware compression, image format, image size, frame rate — and the memory allocated in the delay cache under **Options ‣ Preferences ‣ Capture ‣ Memory**.

If you wish to use a delay that is larger than the maximum that can be set using the slider, increase the size of the memory buffer under **Options ‣ Preferences ‣ Capture ‣ Memory**. Note however that this buffer is always allocated, even if you do not use the delay function.

> [!note]
> When using two capture screens at the same time the memory buffer is shared between the screens.

---
⬆ [[11a Live delay]] · ⬅ [[11a1 Feature description]] · ➡ [[11a3 Recording modes]]
