---
id: "4e3"
title: "Visibility profile"
aliases: ["Visibility profile"]
tags: [kinovea, type/permanent, kinovea/annotation]
up: "[[4e Drawings properties]]"
source: official-manual
---

# Visibility profile

Drawings have a visibility profile that controls their opacity throughout the video.

![[visibilitymenu.png]]

New drawings start with the default opacity options set in **Options ‣ Preferences ‣ Drawings ‣ Opacity**. Each drawing can then be configured to use different visibility options.

In general terms drawings have a fade-in ramp, an opaque section and a fade-out ramp. The default options make drawings fully visible on their key image and fade in and out of the neighboring frames. When drawings are tracked they stay opaque during the section of video where they are tracked.

![[opacity.png]]

## Always visible

With this option the drawing is visible for the entirety of the video. The opaque duration and fading duration options are ignored.

> [!warning]
> The drawing is still attached to the key image it was added to. It will be deleted if the parent key image is deleted.

## Default fading

With this option the drawing uses the default opacity configuration set in **Options ‣ Preferences ‣ Drawings ‣ Opacity**.

## Custom fading

With this option the drawing uses a custom configuration defined through the **Configure custom fading** dialog.

![[customfading.png]]

**Maximum opacity (%)**

This option controls the opacity used during the opaque section. A value of 100 % means the drawing will not let the background show through. A value less than 100 % means the drawing will be somewhat transparent.

**Opaque duration (frames)**

This option controls how long the drawing stays at its maximum opacity level before fading out. This section starts at the keyframe onto which the drawing was added.

**Fading duration (frames)**

This option controls the duration of the ramps before and after the maximum opacity until the drawing becomes completely invisible.

---
⬆ [[4e Drawings properties]] · ⬅ [[4e2 Options and measure labels]]
