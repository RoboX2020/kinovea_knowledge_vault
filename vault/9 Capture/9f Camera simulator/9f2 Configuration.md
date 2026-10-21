---
id: "9f2"
title: "Configuration"
aliases: ["Configuration"]
tags: [kinovea, type/permanent, kinovea/capture]
up: "[[9f Camera simulator]]"
source: official-manual
---

# Configuration

![[config-simulator.png]]

## Stream format

The following stream formats are available:

- **RGB24**: the images are not compressed.

- **JPEG**: the images are compressed.

When using the **JPEG** format, a set of images is compressed in advance and images are rotated to the output. This is to avoid any computer slow downs due to compression when using the simulator to evaluate if a particular camera configuration would be sustainable; as the JPEG compression would be done in the camera.

When using the **RGB24** format, the current time and image sequence number is stamped on the image.

> [!tip]
> You can use the sequential numbers on the images in the recorded video to verify if any frames were dropped during the recording process.

## Width

The width of the images.

## Height

The height of the images.

## Frame rate

The target frame rate of the stream.

---
⬆ [[9f Camera simulator]] · ⬅ [[9f1 General]]
