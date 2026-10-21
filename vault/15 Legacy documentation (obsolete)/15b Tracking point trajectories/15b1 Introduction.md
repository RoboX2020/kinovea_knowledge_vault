---
id: "15b1"
title: "Introduction"
aliases: ["Introduction"]
tags: [kinovea, type/permanent, kinovea/legacy-documentation-obsolete, status/obsolete]
up: "[[15b Tracking point trajectories]]"
source: official-manual-legacy
---

# Introduction

> [!warning] Obsolete
> From the *previous* Kinovea manual. These pages are no longer linked from the official docs and may describe older behavior; they are kept because the current manual's tracking chapters are still empty stubs.

To track the trajectory of a single point or body joint visible on the image follow these steps:

- Right click the object to track and choose **Track path**.

- Move the video forward using the **Next frame** button, the **mouse wheel** or the **Play** button.

- Adjust the point position as necessary during the path creation.

- To finish tracking, right click inside the tracking window and choose **End path edition**.

![[trajectory-basics.jpg]]

Tracking is a semi-automatic process. A candidate point location is computed automatically but can be adjusted manually at any time.

While tracking is in progress two rectangles will be visible around the object being tracked. The inner rectangle is the object window, the outter rectangle is the search window.

![[trajectory-windows.png]]

When the automated tracking fails, correct the point location by dragging the search window. Drag it until the cross at the center of the tracking tool is at the correct location. When tracking resumes, it will use this new point as reference.

> [!tip]
> When the trajectory object is not in path edition mode the trajectory is interactive: clicking on any point of the trajectory will move the video to the corresponding frame.

---
⬆ [[15b Tracking point trajectories]] · ➡ [[15b2 Trajectory options]]
