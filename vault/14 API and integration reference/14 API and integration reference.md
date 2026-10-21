---
id: "14"
title: "API and integration reference"
aliases: ["API and integration reference"]
tags: [kinovea, type/structure, kinovea/api-and-integration-reference, source/code-derived]
up: "[[000 Kinovea Index]]"
source: kinovea-source-code
---

# API and integration reference

Structure note for the **API and integration reference** part.

## Chapters

- [[14a Integration overview]] — Kinovea has no SDK, plugin system or network API.
- [[14b Remote control command reference]] — The official manual explains that commands can be sent through WM_COPYDATA but defers the command list to the Keyboard preferences page inside the application.
    - [[14b1 Protocol]]
    - [[14b2 Finding the window]]
    - [[14b3 Example- Python (ctypes)]]
    - [[14b4 Example- C-]]
    - [[14b5 PlayerScreen commands]]
    - [[14b6 CaptureScreen commands]]
    - [[14b7 Window commands]]
- [[14c UDP network trigger]] — The capture screen can be triggered by a UDP packet, in addition to the audio trigger documented in *Recording triggers*.
    - [[14c1 Behavior]]
    - [[14c2 Example sender]]
- [[14d Command line reference (complete)]] — This supersedes the *Command line options* chapter, which omits several options.
    - [[14d1 Options]]
    - [[14d2 Notes]]
- [[14e KVA file format reference]] — KVA files are UTF-8 XML.
    - [[14e1 Root element and section order]]
    - [[14e2 Conventions]]
    - [[14e3 Practical advice]]
- [[14f Custom posture tool format]] — Every tool in the *Posture* menu (goniometer, human model, bike fit, OpenPose body 25, etc.) is an XML file.
    - [[14f1 Minimal skeleton]]
    - [[14f2 Real example- the shipped Goniometer]]
    - [[14f3 Data section]]
    - [[14f4 Interaction section]]
    - [[14f5 Variables section]]
    - [[14f6 Menus and extras]]
    - [[14f7 Tips]]

---
⬆ [[000 Kinovea Index]] · ⬅ [[13 Miscellaneous topics]] · ➡ [[15 Legacy documentation (obsolete)]]
