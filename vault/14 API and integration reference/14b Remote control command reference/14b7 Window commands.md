---
id: "14b7"
title: "Window commands"
aliases: ["Window commands"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14b Remote control command reference]]"
source: kinovea-source-code
---

# Window commands

These are used internally for communication between Kinovea instances. They are listed for completeness; sending them from outside is possible but rarely useful.

| Message                                | Effect                                                           |
|----------------------------------------|------------------------------------------------------------------|
| `Kinovea:Window.PreferencesUpdated`    | Reload the shared preferences file from disk and refresh the UI. |
| `Kinovea:Window.VariableTableImported` | Reload context variable tables.                                  |
| `Kinovea:Window.CameraUpdated`         | Reload camera aliases/icons.                                     |
| `Kinovea:Window.Close`                 | Close this window (may prompt if annotations are unsaved).       |

---
⬆ [[14b Remote control command reference]] · ⬅ [[14b6 CaptureScreen commands]]
