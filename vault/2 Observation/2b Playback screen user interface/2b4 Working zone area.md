---
id: "2b4"
title: "Working zone area"
aliases: ["Working zone area"]
tags: [kinovea, type/permanent, kinovea/observation]
up: "[[2b Playback screen user interface]]"
source: official-manual
---

# Working zone area

The working zone defines the segment of the video that the player is working with. The play head loops within the working zone.

![[workingzone.png]]

![[timeorigin1.png]] Marks the current time as the time origin. This makes time values relative to this moment.

![[wz_lock.png]] Locks the working zone start and end point to avoid changing them by mistake.

![[wz_left.png]] Sets the starting point of the working zone within the video.

![[wz_right.png]] Sets the ending point of the working zone within the video.

![[wz_reset.png]] Resets the working zone to the whole video.

You can also update the working zone boundaries by directly manipulating the blue end points.

> [!tip]
> If the amount of data fits in the cache memory, the working zone will be loaded in memory.
>
> This improves playback performances and enables the **Video ‣ Overview** and **Video ‣ Reverse** menus. The cache memory can be configured under **Options ‣ Preferences ‣ Playback ‣ Memory**.

---
⬆ [[2b Playback screen user interface]] · ⬅ [[2b3 Annotation toolbar]] · ➡ [[2b5 Timeline area]]
