---
id: "10a4"
title: "Performances"
aliases: ["Performances"]
tags: [kinovea, type/permanent, kinovea/recording]
up: "[[10a Recording options]]"
source: official-manual
---

# Performances

When the recording process is not fast enough to sustain the camera framerate, images are skipped (dropped) and not added to the output video. This can corrupt time measurements made on the output video, as this assumes stable frame rate.

In order to make the most out of the camera without any frame drops, it is important to identify the bottlenecks and configure the camera and Kinovea according to your requirements and the trade offs you are interested in.

Use the infobar to get feedback about performances.

![[infobar2.png]]

See also: [[9b Capture screen user interface|Capture screen user interface]].

## Recording mode

The recording mode **Retroactive** should not yield any frame drops but the duration of the output videos is limited by the amount of memory allocated for the delay buffer. Furthermore, this mode renders the camera unavailable for a small duration after the recording, while Kinovea performs the actual export.

The other two modes record on-the-fly and can record for arbitrary long periods (based on storage space) and without post-recording pause. However they require more configuration if the camera does not already produce compressed images.

## Compression

For cameras that do not produce an already compressed stream, Kinovea may compresses the images on the fly on the CPU. This process is usually slow compared to the frame rate that the camera can sustain.

You can disable compression on recordings under **Options ‣ Preferences ‣ Capture ‣ General**.

When compression is disabled, the amount of data to store on file is between 5 to 10 times larger. In this configuration, the speed of the storage medium might become the new bottleneck. Solid state drives (SSD) are very much recommended instead of hard drives (HDD). NVMe SSD offer even better performances. Ultimately it is also possible to configure a RAM Drive to further increase the storage speed.

---
⬆ [[10a Recording options]] · ⬅ [[10a3 Output options]] · ➡ [[10a5 Automation scenario]]
