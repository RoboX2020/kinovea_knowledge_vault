---
id: "14c1"
title: "Behavior"
aliases: ["Behavior"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14c UDP network trigger]]"
source: kinovea-source-code
---

# Behavior

- Kinovea listens on UDP port **8875** by default (configurable in the capture preferences, under the automation/trigger settings).

- **Any datagram** on that port fires the trigger. The payload is ignored entirely; an empty packet works.

- The trigger must be enabled (it is **off** by default) and armed on the capture screen.

- The configured trigger **quiet period** applies: packets arriving during it are ignored.

- The resulting action is the configured trigger action (default: record video).

- There is no authentication. Anyone on the network who can reach the port can start a recording; firewall accordingly.

---
⬆ [[14c UDP network trigger]] · ➡ [[14c2 Example sender]]
