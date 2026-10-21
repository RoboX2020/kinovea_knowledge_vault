---
id: "4g"
title: "Saving and loading annotation files"
aliases: ["Saving and loading annotation files"]
tags: [kinovea, type/structure, kinovea/annotation]
up: "[[4 Annotation]]"
source: official-manual
---

# Saving and loading annotation files

Annotations are saved in KVA files. These are XML files with a .kva extension.

The term annotation in Kinovea has a broad meaning and encompasses anything that is not directly available in the video file itself. The KVA file stores the following data:

- key images timeline positions, names, color and comments

- drawings attached to key images and their properties

- trajectories, stopwatches, clocks and counters.

- timelines of tracked objects

- image-level overrides such as aspect ratio, rotation or mirroring

- stabilization settings

- spatial calibration

- custom time origin

- capture frame rate

- user override frame rate

- working zone start and end

- the coordinate system object parameters

- background layer opacity and color

- kinogram configuration

- camera motion data

- lens distortion configuration

## Notes in this chapter

- [[4g1 Saving annotations]] — To save the current annotations use the menu File ‣ Save or the shortcut CTRL + S.
- [[4g2 Loading annotations]] — To load an external annotation file into an opened video use the menu File ‣ Load annotations.
- [[4g3 Unloading annotations]] — To completely get rid of all annotations on the current video, including calibration data and other metadata, use the menu Unload annotations.
- [[4g4 Default annotation file]] — To automatically import a specific annotation file into *every* video, you can define a default annotation file.
- [[4g5 Capture annotations]] — When recording video from Kinovea, annotations are automatically created and saved in a sidecar KVA file next to the recorded video file.

---
⬆ [[4 Annotation]] · ⬅ [[4f Inserting images and vector drawings]] · ➡ [[4h Importing external data]]
