---
id: "9a1"
title: "Supported devices"
aliases: ["Supported devices"]
tags: [kinovea, type/permanent, kinovea/capture]
up: "[[9a Introduction]]"
source: official-manual
---

# Supported devices

Kinovea supports the following broad categories of cameras and capture devices:

- [[9c DirectShow compatible devices|DirectShow compatible devices]].

  Webcams and other USB 2.0 cameras, HDMI capture cards and IEEE1394 camcorders.

- [[9d Machine vision cameras|Machine vision cameras]].

  High quality and/or high speed capture devices. USB 3.0 Vision or GigE Vision devices compatible with the GenICam standard.

- [[9e Network cameras and smartphones|Network cameras and smartphones]].

  Anything that can serve MJPEG streams (RTSP streams are not supported).

- [[9f Camera simulator|Camera simulator]].

  A virtual device for testing purposes.

These sub-systems work alongside each other and you may connect multiple devices of different types at the same time.

You can actively stream up to two cameras in a single instance of Kinovea. If you need more than two cameras or if you prefer to dedicate each camera to its own window, you can run multiple instances of Kinovea at the same time and connect one in each instance.

---
⬆ [[9a Introduction]] · ➡ [[9a2 Listing connected cameras]]
