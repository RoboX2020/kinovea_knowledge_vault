---
id: "12c2"
title: "Variables"
aliases: ["Variables"]
tags: [kinovea, type/permanent, kinovea/advanced]
up: "[[12c Post-recording commands]]"
source: official-manual
---

# Variables

Use the button **Insert a variable** to insert context variables that will be replaced with actual values when the command is executed. In addition to the user-defined variables and the date and time built-in variables, the following are available in this context:

| Variable         | Meaning                                                        |
|------------------|----------------------------------------------------------------|
| `%filepath%`     | The full path to the video file.                               |
| `%folderpath%`   | The full path to the capture folder containing the video file. |
| `%filename.ext%` | The name of the recorded file including the extension.         |
| `%filename%`     | The name of the recorded file without the extension.           |
| `%ext%`          | The extension by itself, without the leading dot.              |
| `%kva%`          | The name of the KVA file created alongside the recording.      |

![[prc-insert-variable2.png]]

---
⬆ [[12c Post-recording commands]] · ⬅ [[12c1 Command editor]] · ➡ [[12c3 FFmpeg]]
