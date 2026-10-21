---
id: "4g4"
title: "Default annotation file"
aliases: ["Default annotation file"]
tags: [kinovea, type/permanent, kinovea/annotation]
up: "[[4g Saving and loading annotation files]]"
source: official-manual
---

# Default annotation file

To automatically import a specific annotation file into *every* video, you can define a default annotation file. On the video with the annotations you want to save as default, use the context menu **Save as default player annotations** or **Save as default capture annotations**.

![[default-annotations.png]]

This will create a copy of the file, save it in the application data directory, and add a reference to this location in the preferences under **Options ‣ Preferences ‣ Playback ‣ Default annotation file** or **Options ‣ Preferences ‣ Capture ‣ Default annotation file**.

You can also directly edit this path and point it to a particular file of your choosing.

When opening a new video, if the file exists it will be automatically loaded before any other annotations. The sidecar KVA file will then be merged into it.

---
⬆ [[4g Saving and loading annotation files]] · ⬅ [[4g3 Unloading annotations]] · ➡ [[4g5 Capture annotations]]
