---
id: "12c3"
title: "FFmpeg"
aliases: ["FFmpeg"]
tags: [kinovea, type/permanent, kinovea/advanced]
up: "[[12c Post-recording commands]]"
source: official-manual
---

# FFmpeg

Kinovea ships with the ffmpeg executable that can be used for video conversion and compression.

See the documentation of ffmpeg at <https://ffmpeg.org/> for usage instructions.

Example command that encodes the recorded video using the H.264 codec:

```
ffmpeg -i "%filepath%" -vcodec libx264 "%folderpath%\%filename%_compressed.mp4"
```

---
⬆ [[12c Post-recording commands]] · ⬅ [[12c2 Variables]]
