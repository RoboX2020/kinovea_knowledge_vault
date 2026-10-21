---
id: "5d2"
title: "Capture frame rate"
aliases: ["Capture frame rate"]
tags: [kinovea, type/permanent, kinovea/measurement]
up: "[[5d Time calibration]]"
source: official-manual
---

# Capture frame rate

When a video is captured with a high speed camera (or using the high speed or slow motion function of a smartphone), the generated video file often has a frame rate different from the capture frame rate. For example a video filmed at 1000 fps may be saved to a file with a more typical playback frame rate of 25 fps.

In this case the video will play back slower than real time, which is expected, but the time-related information and calculations would be erroneous if they were based on the playback framerate.

To work with this type of video it is important to configure (or “calibrate”) the time scale. This is done by going to **Video ‣ Configure video timing** and filling the capture frame rate.

![[captureframerate.png]]

Changing this option does not change the nominal speed at which the video is played back. In other words setting the speed control at its mid-point will still play back the video at the same slow motion rate as before. Instead, this option changes the time coordinates of the images.

---
⬆ [[5d Time calibration]] · ⬅ [[5d1 Time origin]] · ➡ [[5d3 Broken playback frame rate]]
