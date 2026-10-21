---
id: "3b"
title: "Synchronization"
aliases: ["Synchronization"]
tags: [kinovea, type/structure, kinovea/comparison]
up: "[[3 Comparison]]"
source: official-manual
---

# Synchronization

The synchronization system supports both synchronized playback and synchronized frame by frame navigation of two videos.

The videos can be heterogenous:

- different frame rates

- different durations

- different image sizes

- different capture frame rates (one video is slow motion and not the other)

## Notes in this chapter

- [[3b1 Synchronization point]] — Two videos can be synchronized by setting their time origin to a common event visible on both videos.
- [[3b2 Joint controls]] — The playback controls are the same as for individual playback screens but act on both videos at the same time.
- [[3b3 Linked speed controls]] — By default the speed controls in each playback screen are linked with each other: lowering the playback speed in one video lowers it in the other.
- [[3b4 Dual replay]] — Normally in the capture-replay workflow the captured video is replayed as soon as possible by the replay screen after it is created.

---
⬆ [[3 Comparison]] · ⬅ [[3a Comparison]]
