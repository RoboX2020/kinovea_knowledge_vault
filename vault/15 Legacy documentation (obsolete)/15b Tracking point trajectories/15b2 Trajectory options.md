---
id: "15b2"
title: "Trajectory options"
aliases: ["Trajectory options"]
tags: [kinovea, type/permanent, kinovea/legacy-documentation-obsolete, status/obsolete]
up: "[[15b Tracking point trajectories]]"
source: official-manual-legacy
---

# Trajectory options

> [!warning] Obsolete
> From the *previous* Kinovea manual. These pages are no longer linked from the official docs and may describe older behavior; they are kept because the current manual's tracking chapters are still empty stubs.

Right click the trajectory object and choose **Configuration** to bring the trajectory settings dialog.

![[trajectory-configuration.png]]

## Visibility

The trajectory visibility can be set to one of the following modes:

- **Complete (A)**: displays the whole trajectory.

- **One second (B)**: displays one second worth of trajectory points.

- **Label (C)**: displays the name of the trajectory in a label.

![[trajectory-visiblity.jpg]]

## Marker

The point at the trajectory position of the current frame can be displayed in one of the following shapes:

- **Cross**

- **Circle**

- **Target**

## Measurement

This option enables the display of a measurement label following the current point on the trajectory. The options are kinematics quantities computed from the trajectory points. This option is also directly available via the trajectory context menu under **Display measure**.

The following options are available:

- **None**

- **Name**

- **Position**

- **Total distance**

- **Total horizontal displacement**

- **Total vertical displacement**

- **Speed**

- **Horizontal velocity**

- **Vertical velocity**

- **Acceleration**

- **Horizontal acceleration**

- **Vertical acceleration**

> [!note]
> To display kinematics measurements in real world units you must first calibrate the coordinate space. If the video is natively in slow motion you must also calibrate the time scale.

## Display rotation circle

This option uses the points of the trajectory to compute the best-fit circle of the trajectory. This is a circle that minimizes the error of each point relatively to a virtual perfect circle.

This can be used to visualize the pseudo-center of a rotary motion.

![[trajectory-circle.png]]

## Tracking

The size of the object and search windows can be modified by dragging the corners of the windows in the preview panel or by changing the values.

The object window should be as small as possible around the point of interest to avoid tracking interferences. The search window should be large enough to contain the position of the point in the next frame, but small enough to avoid interferences between multiple markers.

---
⬆ [[15b Tracking point trajectories]] · ⬅ [[15b1 Introduction]] · ➡ [[15b3 Key images]]
