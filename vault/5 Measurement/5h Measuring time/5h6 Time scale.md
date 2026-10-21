---
id: "5h6"
title: "Time scale"
aliases: ["Time scale"]
tags: [kinovea, type/permanent, kinovea/measurement]
up: "[[5h Measuring time]]"
source: official-manual
---

# Time scale

Videos filmed with high speed cameras or in high speed mode can have a video frame rate different from the capture frame rate. For example a video filmed at 1000 fps is typically saved with a “standard” playback rate of 30 fps. This makes the final video appear in slow motion even when the speed slider is set to 1x.

In this case it is important to tell Kinovea about the original capture frame rate for times to be correct. This impacts time positions and time intervals.

Open the video timing dialog from menu **Video ‣ Configure video timing…** and in the top part of the dialog, enter the capture frame rate.

![[timescale.png]]

> [!note]
> When capturing videos with Kinovea this option is automatically set based on information found in the KVA file saved next to the recording.

---
⬆ [[5h Measuring time]] · ⬅ [[5h5 Time intervals]]
