---
id: "1d4d"
title: "Image naming"
aliases: ["Image naming"]
tags: [kinovea, type/permanent, kinovea/user-interface]
up: "[[1d4 Capture]]"
source: official-manual
---

# Image naming

![[capture_imagenaming.png]]

The options on this page let you configure the automated naming system for image snapshots of the camera stream.

The final path and file name is created by concatenating the **Root**, **Sub directory** and **File** values. Each field can contain special macros referring to context variables that are automatically inserted in the final path.

If no context variable are used at all, the file naming system will prepare the next recording by automatically incrementing a counter and appending a number to the file name.

If the computed value result in the same name as an existing file the capture screen will prompt for overwrite confirmation.

To view the list of available context variables click the **%** button next to the **Sub directory** or **File** fields.

The following context variables are available:

| Macro     | Description                                     |
|-----------|-------------------------------------------------|
| %year     | The current year                                |
| %month    | The current month as a number from 01 to 12.    |
| %day      | The current day of the month from 01 to 31.     |
| %hour     | The current hour from 00 to 23.                 |
| %minute   | The current minute from 00 to 59.               |
| %second   | The current second from 00 to 59.               |
| %date     | The current date in the format “YYYYMMDD”.      |
| %time     | The current time in the format “HHMMSS”.        |
| %datetime | The current date and time as “YYYYMMDD-HHMMSS”. |
| %camalias | The camera alias.                               |
| %camfps   | The configured framerate for the camera.        |
| %recvfps  | The framerate really received from the camera.  |
| %%        | This is replaced by an empty string.            |

Anything that is not exactly part of a macro is copied verbatim to the output. Some examples assuming the current date and time is October 20th, 1968 at 16:00:00 (4 PM):

```
%year-%month-%day: 1968-10-20.
%hour-%minute-%second: 16-00-00.
%datetime: 19681020-160000
%date_text: 19681020_text
%date-%camalias: 19681020-mycamcorder
```

> [!note]
> If you want to use a completely static file name and bypass the automated counter increment for consecutive recordings, use the **%%** macro variable. Be aware that this will require you to either enter the filename manually for every recording or overwrite an existing file.

---
⬆ [[1d4 Capture]] · ⬅ [[1d4c Recording]] · ➡ [[1d4e Video naming]]
