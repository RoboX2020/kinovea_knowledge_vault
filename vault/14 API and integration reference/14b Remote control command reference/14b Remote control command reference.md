---
id: "14b"
title: "Remote control command reference"
aliases: ["Remote control command reference"]
tags: [kinovea, type/structure, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14 API and integration reference]]"
source: kinovea-source-code
---

# Remote control command reference

> [!note]
> This chapter is not part of the official Kinovea manual. It was compiled from the Kinovea source code (github.com/Kinovea/Kinovea, commit `13d0236`, October 2026) to document behavior the manual omits. Where the official manual and the source disagree, the source is what actually runs.

The official manual explains that commands can be sent through `WM_COPYDATA` but defers the command list to the Keyboard preferences page inside the application. This chapter is that list, plus the exact wire protocol.

## Notes in this chapter

- [[14b1 Protocol]]
- [[14b2 Finding the window]] — Each Kinovea window’s title is Kinovea [<name>], where <name> is the window name set in Window ‣ Window properties…, or a name derived from its id if none wa…
- [[14b3 Example- Python (ctypes)]] — WM_COPYDATA = 0x004A
- [[14b4 Example- C-]] — [DllImport("user32.dll", CharSet = CharSet.Unicode)] static extern IntPtr FindWindow(string cls, string title);
[DllImport("user32.dll")] static extern IntPt…
- [[14b5 PlayerScreen commands]] — Default keys are the factory hotkeys; users can rebind them, but remote commands are addressed by name, so rebinding does not affect them.
- [[14b6 CaptureScreen commands]]
- [[14b7 Window commands]] — These are used internally for communication between Kinovea instances.

---
⬆ [[14 API and integration reference]] · ⬅ [[14a Integration overview]] · ➡ [[14c UDP network trigger]]
