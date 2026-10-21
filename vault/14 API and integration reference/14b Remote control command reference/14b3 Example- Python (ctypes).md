---
id: "14b3"
title: "Example- Python (ctypes)"
aliases: ["Example- Python (ctypes)"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14b Remote control command reference]]"
source: kinovea-source-code
---

# Example- Python (ctypes)

```python
import ctypes
from ctypes import wintypes

WM_COPYDATA = 0x004A

class COPYDATASTRUCT(ctypes.Structure):
    _fields_ = [("dwData", ctypes.c_size_t),
                ("cbData", wintypes.DWORD),
                ("lpData", ctypes.c_void_p)]

def send(command, window_title="Kinovea [Replay]"):
    hwnd = ctypes.windll.user32.FindWindowW(None, window_title)
    if not hwnd:
        raise RuntimeError("Kinovea window not found: " + window_title)
    buf = ctypes.create_unicode_buffer("Kinovea:" + command)   # UTF-16, NUL-terminated
    cds = COPYDATASTRUCT(0, ctypes.sizeof(buf), ctypes.cast(buf, ctypes.c_void_p))
    ctypes.windll.user32.SendMessageW(hwnd, WM_COPYDATA, 0, ctypes.byref(cds))

send("CaptureScreen.ToggleRecording")
```

---
⬆ [[14b Remote control command reference]] · ⬅ [[14b2 Finding the window]] · ➡ [[14b4 Example- C-]]
