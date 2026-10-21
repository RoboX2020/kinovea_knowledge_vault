---
id: "1d2c1"
title: "Time"
aliases: ["Time"]
tags: [kinovea, type/permanent, kinovea/user-interface]
up: "[[1d2c Units]]"
source: official-manual
---

# Time

This option controls the format of all time-related information displayed in the program [^1]. It is used in the timeline position and duration, in chronometers and clocks, and in exported files.

The following options are available:

| Format                                 | Example        | Description                     |
|----------------------------------------|----------------|---------------------------------|
| \[h:\]\[mm:\]ss.xx\[x\]                | 1:10.48        | Textual timecode.               |
| Frame number                           | 1762           | Rank of the current frame.      |
| Total milliseconds                     | 70480          | Integer number of milliseconds. |
| Total microseconds                     | 1284           | Integer number of microseconds. |
| Ten thousandth of an hour              | 904            | Ten thousandths of an hour      |
| Hundredth of a minute                  | 542            | Hundredths of a minute          |
| \[h:\]\[mm:\]ss.xx\[x\] + Frame number | 1:10.48 (1762) |                                 |

When using textual timecode if the real time framerate is higher than 100 fps, thousandths of seconds are displayed. Hours and minutes are only displayed when necessary.

> [!note]
> The time starts at the **time origin**. The time origin can be configured to be anywhere in the video. Video locations that are before the time origin are displayed as negative numbers. If the time origin is not manually defined, the time origin is automatically set to the start of the current video section.

---
⬆ [[1d2c Units]] · ➡ [[1d2c2 Speed]]
