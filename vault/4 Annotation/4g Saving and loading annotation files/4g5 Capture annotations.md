---
id: "4g5"
title: "Capture annotations"
aliases: ["Capture annotations"]
tags: [kinovea, type/permanent, kinovea/annotation]
up: "[[4g Saving and loading annotation files]]"
source: official-manual
---

# Capture annotations

When recording video from Kinovea, annotations are automatically created and saved in a sidecar KVA file next to the recorded video file. This file contains the capture frame rate, the camera rotation and mirror options, and the time origin is set to the start of the recording (ex: trigger time).

If drawings were added in the capture screen, they are also saved in this KVA file. It is possible to disable this behavior in **Options ‣ Preferences ‣ Capture ‣ Recording ‣ Exported annotations**.

In a capture-replay workflow, if these drawings are modified on the player side and saved, it is possible to send them back to the capture screen using the following menu on the capture screen **Reload linked annotations**. Only drawings on the first key image are reloaded, as the capture screen only has one key image.

This workflow can be useful in a self-training context: posture guides can be adjusted on the recorded video much easier compared to the live camera feed.

---
⬆ [[4g Saving and loading annotation files]] · ⬅ [[4g4 Default annotation file]]
