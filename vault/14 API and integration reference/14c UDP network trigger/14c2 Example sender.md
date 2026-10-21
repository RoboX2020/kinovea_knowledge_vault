---
id: "14c2"
title: "Example sender"
aliases: ["Example sender"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14c UDP network trigger]]"
source: kinovea-source-code
---

# Example sender

This is the test client shipped in the Kinovea repository (`Tools/remote/udp-client.py`), slightly generalized:

```python
import socket

def fire(host="192.168.0.228", port=8875):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # allows broadcast addresses too
    s.sendto(b"", (host, port))
    s.close()

fire()
```

Typical uses: a timing gate, force plate or microcontroller (ESP32, Arduino with Ethernet) signalling the moment of interest. Combine with the capture delay buffer so the recording includes the moments *before* the trigger.

---
⬆ [[14c UDP network trigger]] · ⬅ [[14c1 Behavior]]
