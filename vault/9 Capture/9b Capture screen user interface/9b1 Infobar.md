---
id: "9b1"
title: "Infobar"
aliases: ["Infobar"]
tags: [kinovea, type/permanent, kinovea/capture]
up: "[[9b Capture screen user interface]]"
source: official-manual
---

# Infobar

The infobar contains information about the connected camera and streaming performances.

![[infobar1.png]]

The first part of the infobar displays the alias of the camera and the current configuration for image size, frame rate and image format. Clicking in this area of the infobar will bring up the camera configuration dialog.

The frame rate indicated is the one configured, the actual frame rate sent by the camera might be different for various reasons like low light levels or hardware limitations.

The second part of the infobar displays the following live statistics:

![[infobar2.png]]

## Signal (fps)

This is the frequency at which Kinovea is receiving images from the camera. The value is in frames per second.

Many cameras will reduce their frame rate based on various external factors. For example, when a camera uses auto-exposure and the exposure duration computed by the device is incompatible with the selected frame rate.

## Throughput (MB/s)

This is the amount of data that passes through Kinovea as it processes the stream. The value is in megabytes per second, with the convention of one megabyte as 1024 kilobytes.

This value is related to the the image size, frame rate and format, possible on-camera image compression, link bandwidth, and possible post-processing done at the driver level.

You can use this value to estimate the necessary speed for your storage medium to write the uncompressed stream.

In the case of a non-compressed stream in RGB24 format, the value is calculated as follows:

`Throughput = (width × height × 3 × frame rate) / (1024*1024)`

## Load (%)

This value describes how much Kinovea is struggling to keep up with the camera framerate. It is computed as the time taken to process one frame divided by the interval between frames.

When this value is near 100% it means it takes Kinovea the same amount of time to process one frame as the time budget it has for that frame, if it goes over 100% dropped frames may occur.

## Drops

This is the number of frames that could not be processed by Kinovea during the current or last recording session.

If this value is non-zero, some frames are missing from the output video and any measurements involving time will not be perfectly accurate.

---
⬆ [[9b Capture screen user interface]] · ➡ [[9b2 Context bar]]
