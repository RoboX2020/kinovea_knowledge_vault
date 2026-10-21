---
id: "14b5"
title: "PlayerScreen commands"
aliases: ["PlayerScreen commands"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14b Remote control command reference]]"
source: kinovea-source-code
---

# PlayerScreen commands

Default keys are the factory hotkeys; users can rebind them, but remote commands are addressed by name, so rebinding does not affect them.

| Message                                           | Default key       | Effect                                                                                                                                                                   |
|---------------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Kinovea:PlayerScreen.ResetViewport`              | Esc               | Reset the viewport (exit zoom, close menus).                                                                                                                             |
| `Kinovea:PlayerScreen.Close`                      | Ctrl + F4         | Close the screen.                                                                                                                                                        |
| `Kinovea:PlayerScreen.TogglePlay`                 | Space             | Start/stop playback.                                                                                                                                                     |
| `Kinovea:PlayerScreen.IncreaseSpeed10`            | Up                | Increase playback speed by 10%.                                                                                                                                          |
| `Kinovea:PlayerScreen.DecreaseSpeed10`            | Down              | Decrease playback speed by 10%.                                                                                                                                          |
| `Kinovea:PlayerScreen.IncreaseSpeed1`             | Shift + Up        | Increase playback speed by 1%.                                                                                                                                           |
| `Kinovea:PlayerScreen.DecreaseSpeed1`             | Shift + Down      | Decrease playback speed by 1%.                                                                                                                                           |
| `Kinovea:PlayerScreen.GotoPreviousImage`          | Left              | Step one frame backward.                                                                                                                                                 |
| `Kinovea:PlayerScreen.GotoNextImage`              | Right             | Step one frame forward.                                                                                                                                                  |
| `Kinovea:PlayerScreen.GotoFirstImage`             | Home              | Go to the first frame.                                                                                                                                                   |
| `Kinovea:PlayerScreen.GotoLastImage`              | End               | Go to the last frame.                                                                                                                                                    |
| `Kinovea:PlayerScreen.GotoPreviousImageForceLoop` | Shift + Left      | Step backward, wrapping to the end at the start.                                                                                                                         |
| `Kinovea:PlayerScreen.LargeJumpBackward`          | Page Up           | Large jump backward.                                                                                                                                                     |
| `Kinovea:PlayerScreen.LargeJumpForward`           | Page Down         | Large jump forward.                                                                                                                                                      |
| `Kinovea:PlayerScreen.SmallJumpBackward`          | Shift + Page Up   | Small jump backward.                                                                                                                                                     |
| `Kinovea:PlayerScreen.SmallJumpForward`           | Shift + Page Down | Small jump forward.                                                                                                                                                      |
| `Kinovea:PlayerScreen.GotoPreviousKeyframe`       | Ctrl + Left       | Go to the previous key image.                                                                                                                                            |
| `Kinovea:PlayerScreen.GotoNextKeyframe`           | Ctrl + Right      | Go to the next key image.                                                                                                                                                |
| `Kinovea:PlayerScreen.GotoSyncPoint`              | F8                | Go to the synchronization point.                                                                                                                                         |
| `Kinovea:PlayerScreen.IncreaseSyncAlpha`          | Alt + Num +       | Increase merge opacity in dual mode.                                                                                                                                     |
| `Kinovea:PlayerScreen.DecreaseSyncAlpha`          | Alt + Num −       | Decrease merge opacity in dual mode.                                                                                                                                     |
| `Kinovea:PlayerScreen.ToggleSyncMerge`            | F9                | **No effect via remote control.** The player screen has no handler for it; superposition is handled by the dual-player controller, which external messages do not reach. |
| `Kinovea:PlayerScreen.IncreaseZoom`               | Ctrl + Num +      | Zoom in.                                                                                                                                                                 |
| `Kinovea:PlayerScreen.DecreaseZoom`               | Ctrl + Num −      | Zoom out.                                                                                                                                                                |
| `Kinovea:PlayerScreen.ResetZoom`                  | Ctrl + Num 0      | Reset zoom.                                                                                                                                                              |
| `Kinovea:PlayerScreen.AddKeyframe`                | Ins               | Add a key image at the current frame.                                                                                                                                    |
| `Kinovea:PlayerScreen.DeleteKeyframe`             | Ctrl + Del        | Delete the key image at the current frame.                                                                                                                               |
| `Kinovea:PlayerScreen.Preset1`                    | Ctrl + Num 1      | Apply key image preset 1.                                                                                                                                                |
| `Kinovea:PlayerScreen.Preset2`                    | Ctrl + Num 2      | Apply key image preset 2.                                                                                                                                                |
| `Kinovea:PlayerScreen.Preset3`                    | Ctrl + Num 3      | Apply key image preset 3.                                                                                                                                                |
| `Kinovea:PlayerScreen.Preset4`                    | Ctrl + Num 4      | Apply key image preset 4.                                                                                                                                                |
| `Kinovea:PlayerScreen.Preset5`                    | Ctrl + Num 5      | Apply key image preset 5.                                                                                                                                                |
| `Kinovea:PlayerScreen.Preset6`                    | Ctrl + Num 6      | Apply key image preset 6.                                                                                                                                                |
| `Kinovea:PlayerScreen.Preset7`                    | Ctrl + Num 7      | Apply key image preset 7.                                                                                                                                                |
| `Kinovea:PlayerScreen.Preset8`                    | Ctrl + Num 8      | Apply key image preset 8.                                                                                                                                                |
| `Kinovea:PlayerScreen.Preset9`                    | Ctrl + Num 9      | Apply key image preset 9.                                                                                                                                                |
| `Kinovea:PlayerScreen.Preset10`                   | —                 | Apply key image preset 10.                                                                                                                                               |
| `Kinovea:PlayerScreen.CutDrawing`                 | Ctrl + X          | Cut the selected drawing.                                                                                                                                                |
| `Kinovea:PlayerScreen.CopyDrawing`                | Ctrl + C          | Copy the selected drawing.                                                                                                                                               |
| `Kinovea:PlayerScreen.PasteDrawing`               | Ctrl + V          | Paste drawing at the mouse position.                                                                                                                                     |
| `Kinovea:PlayerScreen.PasteInPlaceDrawing`        | —                 | Paste drawing at its original position.                                                                                                                                  |
| `Kinovea:PlayerScreen.DeleteDrawing`              | Del               | Delete the selected drawing.                                                                                                                                             |
| `Kinovea:PlayerScreen.ValidateDrawing`            | Enter             | Finish the drawing in progress.                                                                                                                                          |
| `Kinovea:PlayerScreen.CopyImage`                  | Ctrl + Shift + C  | Copy the current image to the clipboard.                                                                                                                                 |
| `Kinovea:PlayerScreen.CopyTime`                   | —                 | Copy the current time to the clipboard.                                                                                                                                  |
| `Kinovea:PlayerScreen.ToggleDrawingsVisibility`   | —                 | Show/hide all drawings.                                                                                                                                                  |
| `Kinovea:PlayerScreen.ChronometerStartStop`       | F5                | Start/stop the active stopwatch.                                                                                                                                         |
| `Kinovea:PlayerScreen.ChronometerSplit`           | F6                | Record a split on the active stopwatch.                                                                                                                                  |
| `Kinovea:PlayerScreen.CadenceBeat`                | F7                | Add a beat to the cadence counter.                                                                                                                                       |
| `Kinovea:PlayerScreen.StartAllTracking`           | —                 | Start tracking for all trackable drawings.                                                                                                                               |

---
⬆ [[14b Remote control command reference]] · ⬅ [[14b4 Example- C-]] · ➡ [[14b6 CaptureScreen commands]]
