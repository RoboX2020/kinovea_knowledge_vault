---
id: "14a"
title: "Integration overview"
aliases: ["Integration overview"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14 API and integration reference]]"
source: kinovea-source-code
---

# Integration overview

> [!note]
> This chapter is not part of the official Kinovea manual. It was compiled from the Kinovea source code (github.com/Kinovea/Kinovea, commit `13d0236`, October 2026) to document behavior the manual omits. Where the official manual and the source disagree, the source is what actually runs.

Kinovea has no SDK, plugin system or network API. Third-party programs integrate with it through five mechanisms:

| Mechanism                           | Direction                                  | Use it to…                                                                                                                  |
|-------------------------------------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Window messages (`WM_COPYDATA`)     | Your program → running Kinovea             | Drive playback, recording, delay, zoom, drawings: any of 75 commands.                                                       |
| UDP trigger                         | Any device on the network → capture screen | Fire the capture trigger (start recording) from a network packet.                                                           |
| Command line                        | Launcher → new Kinovea process             | Open videos, set speed, restore a named window.                                                                             |
| Post-recording command              | Kinovea → your program                     | Run a shell command after each recording, with file path variables (see the *Post-recording commands* chapter in Advanced). |
| Files (KVA, posture tools, exports) | Both ways                                  | Read or write annotations, define custom drawing tools, consume CSV/XML exports.                                            |

All of these are Windows-only, like Kinovea itself.

---
⬆ [[14 API and integration reference]] · ➡ [[14b Remote control command reference]]
