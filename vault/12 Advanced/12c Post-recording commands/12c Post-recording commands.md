---
id: "12c"
title: "Post-recording commands"
aliases: ["Post-recording commands"]
tags: [kinovea, type/structure, kinovea/advanced]
up: "[[12 Advanced]]"
source: official-manual
---

# Post-recording commands

Post-recording commands let you execute external programs right after a recording is finalized. The created file can be passed as an argument to the external program.

Some use cases include:

- copying the file to a backup location.

- converting the recorded file to a different format.

- running a post-processing application to transform the video in some way or extract images.

## Notes in this chapter

- [[12c1 Command editor]] — To enable post-recording commands right click the background of a capture screen and choose the menu Post-recording command….
- [[12c2 Variables]] — Use the button Insert a variable to insert context variables that will be replaced with actual values when the command is executed.
- [[12c3 FFmpeg]] — Kinovea ships with the ffmpeg executable that can be used for video conversion and compression.

---
⬆ [[12 Advanced]] · ⬅ [[12b Workspaces]] · ➡ [[12d Command line options]]
