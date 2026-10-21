---
id: "4h1"
title: "OpenPose"
aliases: ["OpenPose"]
tags: [kinovea, type/permanent, kinovea/annotation]
up: "[[4h Importing external data]]"
source: official-manual
---

# OpenPose

OpenPose is a software that detects human body poses in images.

To learn more about OpenPose check the project page: <https://github.com/CMU-Perceptual-Computing-Lab/openpose>

The result of running the OpenPose program on a video is a set of JSON files containing data for one or more human postures. OpenPose uses a 25-point body model.

This is not meant to be used for measurements but for general posture assessment.

The workflow to import OpenPose data into Kinovea is the following:

Run the OpenPose software on the video, using the write_json option. This creates a set of .json files in the output directory. Each file contains descriptors for the detected poses.

```
> bin\OpenPoseDemo.exe --video examples\media\video.avi --write_json output/
```

In Kinovea, use the menu **File ‣ Load annotations…** and point to the first JSON file of the series.

Each detected human pose will be converted to a human model drawing using a dedicated model.

![[openpose.png]]

---
⬆ [[4h Importing external data]] · ➡ [[4h2 SRT SubRip Text subtitles]]
