---
id: "5d3"
title: "Broken playback frame rate"
aliases: ["Broken playback frame rate"]
tags: [kinovea, type/permanent, kinovea/measurement]
up: "[[5d Time calibration]]"
source: official-manual
---

# Broken playback frame rate

In some cases a video is saved with a frame rate which is just plain wrong, or Kinovea cannot read it. For example a USB camera might claim that it is capturing video at 25 fps but the video stream is actually transfered at 15 fps.

In this case the video will play back at the wrong speed and the time calibration will be wrong. If you know the real playback frame rate at which the video is supposed to be played back, you may enter it in **Video ‣ Configure video timing**.

![[brokenframerate.png]]

Changing this option does change the nominal speed at which the video is played back.

---
⬆ [[5d Time calibration]] · ⬅ [[5d2 Capture frame rate]]
