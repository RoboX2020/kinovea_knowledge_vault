---
id: "1d4b"
title: "Memory"
aliases: ["Memory"]
tags: [kinovea, type/permanent, kinovea/user-interface]
up: "[[1d4 Capture]]"
source: official-manual
---

# Memory

![[capture_memory.png]]

## Memory allocated for delay buffers

This option controls the amount of memory used to remember old frames, in the context of the delayed view of the camera feed. By extension, this option defines the maximum delay configurable in the capture screen. The maximum delay is based on image size, image format and capture framerate.

When using two capture screens at the same time each screen uses half the memory amount configured.

In the case of multiple instances of Kinovea, each instance has its own delay buffer memory.

> [!warning]
> Unlike the cache memory in the playback screen, this amount of memory is always allocated and used as soon as a capture screen is opened.

---
⬆ [[1d4 Capture]] · ⬅ [[1d4a General]] · ➡ [[1d4c Recording]]
