---
id: "14b1"
title: "Protocol"
aliases: ["Protocol"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14b Remote control command reference]]"
source: kinovea-source-code
---

# Protocol

- **Message:** `WM_COPYDATA` (`0x004A`) sent with `SendMessage` to the Kinovea main window.

- **dwData:** must be `0`. Any other value is rejected as malformed.

- **lpData / cbData:** the command string, NUL-terminated. Both UTF-16 (wide) and ANSI encodings are accepted: Kinovea tries UTF-16 first, then ANSI.

- **Format:** `Kinovea:<Category>.<Command>`. Everything before the first `:` must be `Kinovea`; the payload must split into exactly two non-empty tokens on `.`.

- **Categories:** only `PlayerScreen`, `CaptureScreen` and `Window` are dispatched. Other category names shown in the Keyboard preferences (`FileExplorer`, `ThumbnailViewer…`, `DualPlayer`, `DualCapture`) are hotkey-only and **cannot** be triggered remotely.

- **Names are case-sensitive** (parsed with `Enum.TryParse` without ignore-case). `toggleplay` fails; `TogglePlay` works.

- **Fan-out:** a `PlayerScreen` command is executed on *every* open player screen; a `CaptureScreen` command on *every* capture screen. There is no way to target only the left or right screen.

- **No reply.** `SendMessage` returns when the message is handled, but no status is returned. Failures appear only in Kinovea’s log file.

- **Minimized windows** still receive and execute commands. Kinovea explicitly allows `WM_COPYDATA` through UIPI (`ChangeWindowMessageFilterEx`), so a non-elevated sender can talk to an elevated Kinovea.

---
⬆ [[14b Remote control command reference]] · ➡ [[14b2 Finding the window]]
