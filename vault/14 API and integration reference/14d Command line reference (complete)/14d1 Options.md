---
id: "14d1"
title: "Options"
aliases: ["Options"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14d Command line reference (complete)]]"
source: kinovea-source-code
---

# Options

| Option                   | Meaning                                                                                                                                                                                                                 |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-name <string>`         | Restore the saved window with this name. Takes precedence over every other option: if present, `-video` etc. are ignored.                                                                                               |
| `-id <string>`           | Restore the saved window with this id. Used internally; checked after `-name`.                                                                                                                                          |
| `-video <path>`          | Load and **autoplay** this video in a player screen.                                                                                                                                                                    |
| `-video2 <path>`         | *Undocumented in the manual.* Load a second video in a second player screen (dual mode). Requires `-video`.                                                                                                             |
| `-speed <n>`             | Playback speed as a percentage of the original frame rate, applied to both videos. The manual says `0..200`; the code actually clamps to **1–1000**. Unparseable values fall back to 100. Use `.` as decimal separator. |
| `-stretch`               | Expand the video(s) to fit the screen.                                                                                                                                                                                  |
| `-hideExplorer`          | Hide the navigation pane.                                                                                                                                                                                               |
| `<file>` (sole argument) | *Undocumented.* If the only argument is an existing file, it is opened in a single player with autoplay **and stretch**. This is what happens when a file is dropped on `kinovea.exe`.                                  |
| `-help`, `-h`            | *Undocumented.* Print usage to the parent console.                                                                                                                                                                      |

---
⬆ [[14d Command line reference (complete)]] · ➡ [[14d2 Notes]]
