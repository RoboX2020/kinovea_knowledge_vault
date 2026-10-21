---
id: "1d2a"
title: "General"
aliases: ["General"]
tags: [kinovea, type/permanent, kinovea/user-interface]
up: "[[1d2 Playback]]"
source: official-manual
---

# General

![[playback_general.png]]

## Import image sequences as videos

When this option is enabled and an image file is opened, Kinovea will try to detect an **image sequence** by looking for consecutive numbers in the name of other files of the same folder. If an image sequence is detected, all the image files will automatically be loaded and the whole collection interpreted as a video.

Example of file names interpreted as a sequence:

- image_001.png, image_002.png, image_003.png, etc.

- test01.jpg, test02.jpg, test03.jpg, etc.

The numbers can be anywhere in the file name. Aside from the numbers the rest of the name should be identical for all files. The amount of leading zeroes in the numbering scheme should be consistent between all files of the sequence.

A gap or a change in the numbering system will be interpreted as the end of the sequence. The detection is bidirectional: any file can be used to load the sequence, the resulting video will always start at the file with the lower number found.

## Link speed sliders when comparing videos

When this option is checked and two videos are compared, changing the playback speed in one player will automatically change the playback speed in the other player to match it.

> [!note]
> The playback speed is matched according to the real time speed, taking into account differences in video file framerate and capture framerate. If one video is in slow motion and the other is at normal speed, this option should still work as expected as long as the capture framerate of the slow motion video is correctly configured.

## Update image during time cursor movement

When this option is not checked the video display will be paused when manually moving the timeline cursor.

## Default aspect ratio

This option defines the default image aspect ratio configured any time a video file is opened. It is the same as manually configuring the menu **Image ‣ Image format**.

The following options are available:

- **Auto detection**

- **Force 4:3**

- **Force 16:9**

The **Auto detection** option uses the image size and the pixel aspect ratio found in the video file metadata to calculate the image height. The other options will change the height of the video to match a 4:3 or 16:9 aspect ratio.

## Always deinterlace when opening a new video

This option forces the deinterlacing mechanism to be enabled for all opened files. It is the same as manually configuring the menu **Image ‣ Deinterlace**.

## Default annotations file

This option lets you point to a .KVA file containing video annotations that will be automatically loaded when any video is opened.

Other annotations files can still be loaded on top of the video by using the sidecar file method or through the menu **File ‣ Load annotations**. They will be merged with each others.

See also: [[4g Saving and loading annotation files|Saving and loading annotation files]].

---
⬆ [[1d2 Playback]] · ➡ [[1d2b Memory]]
