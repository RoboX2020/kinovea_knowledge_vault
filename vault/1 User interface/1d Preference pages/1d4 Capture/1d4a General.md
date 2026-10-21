---
id: "1d4a"
title: "General"
aliases: ["General"]
tags: [kinovea, type/permanent, kinovea/user-interface]
up: "[[1d4 Capture]]"
source: official-manual
---

# General

![[capture_general.png]]

## Record uncompressed video

When this option is checked the video are recorded without compressing the video frames to JPEG first. When this option is unchecked the video frames are compressed to JPEG using high quality settings to retain fidelity.

This option can be used to minimize dropped frames, by trading off space for speed (due to the JPEG settings used, image quality shouldn’t really be much impacted by this option). When using a fast storage medium it can be faster to store the large uncompressed images compared to the time it takes to compress them.

For image snapshots the compression depends on the file format.

> [!note]
> When configuring cameras to use MJPEG streams this option is ignored. The MJPEG streams are always saved as-is in their container format.

> [!note]
> When configuring cameras to use raw Bayer pattern images you must enable this option to be able to reconstruct the color information at playback time.

> [!warning]
> Not all video players can play back uncompressed files.

## Display framerate

This option defines the frequency at which the camera images are updated in the capture screen.

While recording the computer resources are shared between displaying the camera stream and recording it to the storage medium. The highest priority is always given to recording but lowering this value can help reduce the overall load on the computer and improve recording performance.

## Image format

This option defines the default image format used when saving snapshots.

The following image formats are available:

- **JPG**

- **PNG**

- **BMP**

## Video format

This option defines the default video container format used when recording compressed videos. All videos are compressed using an MJPEG codec.

The following container formats are available:

- **MP4**

- **AVI**

- **MKV**

## Uncompressed video format

This option defines the default video container format used when recording uncompressed videos.

The following container formats are available:

- **MKV**

- **AVI**

## Default annotations file

This option lets you point to a .KVA file containing annotations that will be automatically loaded when any camera stream is opened.

Other annotations files can still be loaded on top of the camera stream by using the menu **File ‣ Load annotations**. They will be merged with each others.

See also: [[4g Saving and loading annotation files|Saving and loading annotation files]].

---
⬆ [[1d4 Capture]] · ➡ [[1d4b Memory]]
