---
id: "11b1"
title: "Feature description"
aliases: ["Feature description"]
tags: [kinovea, type/permanent, kinovea/delay-and-replay]
up: "[[11b Instant replay mechanism]]"
source: official-manual
---

# Feature description

Replay folder observers are special playback screens that constantly monitor a specific folder for new videos. When a new video is created in the monitored folder, the playback screen automatically loads it and starts playing it. This can be used to automate the capture and replay the feedback loop.

The replay folder observer works at the file system level and is independent from the source or process creating the video. The videos can be created by the same or another instance of Kinovea, or by an external process.

Apart from the monitoring mechanism, the video is loaded normally. In particular the annotation file created by the capture screen is loaded and drawings created on the capture side are imported.

---
⬆ [[11b Instant replay mechanism]] · ➡ [[11b2 Creating a replay observer]]
