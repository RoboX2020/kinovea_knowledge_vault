---
id: "1d4c"
title: "Recording"
aliases: ["Recording"]
tags: [kinovea, type/permanent, kinovea/user-interface]
up: "[[1d4 Capture]]"
source: official-manual
---

# Recording

![[capture_recording.png]]

## Recording mode and delay

The recording mode option defines how the recording sub-system interacts with the delay buffer to create the output video.

When the camera transmits a new frame it is always put in the delay buffer and the recording sub-system always takes frames from the delay buffer to create the output video.

### Camera

When using this recording mode the delay value set in the capture screen is ignored.

Recording is performed on the fly, the saved frame is always the most recent frame sent by the camera.

> [!tip]
> If you do not require recording of delayed images this option can result in slightly better performances than the Delayed method.

### Delayed

When using this recording mode the delay value set in the capture screen is taken into account.

Recording is performed on the fly, the saved frame is taken from the delay buffer based on the delay value.

This can be used to record actions happening before the moment the record button is hit or triggered.

### Retroactive

When using this recording mode the recording is not performed on the fly. Instead, at the end of the recording process, when clicking the stop recording button or when the maximum recording duration is reached, the camera feed is paused, the delay buffer is frozen, and the video file is created all at once.

The delay value is taken into account for creating the recording.

This mode offers the best recording performances and minimizes dropped frames, at the cost of a reduced maximum length for created videos and a temporary freezing of the camera feed.

> [!tip]
> The maximum length of recorded videos using this recording mode depends on the size of the delay buffer. This can be configured from the Memory preference page.

## High speed cameras

The options in this group let you alter the framerate written in the metadata of the output file. This influences the amount of resources required to replay the file and the apparent speed of the action.

A camera might be capable of producing and transmitting 1000 frames per second but the computer will not be able to play the file back at that speed and the monitor won’t be able to refresh itself fast enough either. To work around this problem it is usual to reduce the framerate of the output file to a more typical one. Recording devices normally apply this transformation automatically. This results in a video that appears to be in slow motion.

### Framerate replacement threshold

This option controls the framerate from which the output file is modified to use a lower one.

If the camera is configured to send images at a higher framerate than this value, the actual framerate stored in the file metadata will be the replacement framerate. If the camera is configured to send images at a lower framerate than this value, no change will happen.

### Replacement framerate

This value defines the final framerate written in the file metadata when the framerate configured in the camera is above the threshold.

---
⬆ [[1d4 Capture]] · ⬅ [[1d4b Memory]] · ➡ [[1d4d Image naming]]
