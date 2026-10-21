---
id: "14b2"
title: "Finding the window"
aliases: ["Finding the window"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14b Remote control command reference]]"
source: kinovea-source-code
---

# Finding the window

Each Kinovea window’s title is `Kinovea [<name>]`, where `<name>` is the window name set in **Window ‣ Window properties…**, or a name derived from its id if none was set. Locate it with `FindWindow(NULL, "Kinovea [Replay]")`. Naming your windows makes scripting much easier.

---
⬆ [[14b Remote control command reference]] · ⬅ [[14b1 Protocol]] · ➡ [[14b3 Example- Python (ctypes)]]
