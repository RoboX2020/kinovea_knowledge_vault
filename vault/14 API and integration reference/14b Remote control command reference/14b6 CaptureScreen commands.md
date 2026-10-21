---
id: "14b6"
title: "CaptureScreen commands"
aliases: ["CaptureScreen commands"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14b Remote control command reference]]"
source: kinovea-source-code
---

# CaptureScreen commands

| Message                                         | Default key       | Effect                                       |
|-------------------------------------------------|-------------------|----------------------------------------------|
| `Kinovea:CaptureScreen.ResetViewport`           | Esc               | Reset the viewport (exit zoom, close menus). |
| `Kinovea:CaptureScreen.OpenConfiguration`       | F12               | Open the camera configuration dialog.        |
| `Kinovea:CaptureScreen.Close`                   | Ctrl + F4         | Close the screen.                            |
| `Kinovea:CaptureScreen.ToggleGrabbing`          | Space             | Pause/resume the camera stream.              |
| `Kinovea:CaptureScreen.ToggleRecording`         | Ctrl + Enter      | Start/stop recording.                        |
| `Kinovea:CaptureScreen.TakeSnapshot`            | Shift + Enter     | Save a snapshot image.                       |
| `Kinovea:CaptureScreen.ToggleArmCaptureTrigger` | —                 | Arm/disarm the capture trigger.              |
| `Kinovea:CaptureScreen.IncreaseZoom`            | —                 | Zoom in.                                     |
| `Kinovea:CaptureScreen.DecreaseZoom`            | —                 | Zoom out.                                    |
| `Kinovea:CaptureScreen.ResetZoom`               | —                 | Reset zoom.                                  |
| `Kinovea:CaptureScreen.GotoPreviousImage`       | Left              | Step one frame backward.                     |
| `Kinovea:CaptureScreen.GotoNextImage`           | Right             | Step one frame forward.                      |
| `Kinovea:CaptureScreen.GotoFirstImage`          | Home              | Go to the first frame.                       |
| `Kinovea:CaptureScreen.GotoLastImage`           | End               | Go to the last frame.                        |
| `Kinovea:CaptureScreen.BackwardRound10Percent`  | Page Up           | Move back 10% in the delay buffer.           |
| `Kinovea:CaptureScreen.ForwardRound10Percent`   | Page Down         | Move forward 10% in the delay buffer.        |
| `Kinovea:CaptureScreen.BackwardRound1Percent`   | Shift + Page Up   | Move back 1% in the delay buffer.            |
| `Kinovea:CaptureScreen.ForwardRound1Percent`    | Shift + Page Down | Move forward 1% in the delay buffer.         |
| `Kinovea:CaptureScreen.ToggleDelayedDisplay`    | Alt + Home        | Toggle the delayed display.                  |
| `Kinovea:CaptureScreen.IncreaseDelayOneSecond`  | Up                | Increase delay by 1 s.                       |
| `Kinovea:CaptureScreen.DecreaseDelayOneSecond`  | Down              | Decrease delay by 1 s.                       |
| `Kinovea:CaptureScreen.IncreaseDelayOneFrame`   | Ctrl + Up         | Increase delay by one frame.                 |
| `Kinovea:CaptureScreen.DecreaseDelayOneFrame`   | Ctrl + Down       | Decrease delay by one frame.                 |
| `Kinovea:CaptureScreen.IncreaseDelayHalfSecond` | Shift + Up        | Increase delay by 0.5 s.                     |
| `Kinovea:CaptureScreen.DecreaseDelayHalfSecond` | Shift + Down      | Decrease delay by 0.5 s.                     |

---
⬆ [[14b Remote control command reference]] · ⬅ [[14b5 PlayerScreen commands]] · ➡ [[14b7 Window commands]]
