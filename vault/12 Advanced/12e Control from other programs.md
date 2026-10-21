---
id: "12e"
title: "Control from other programs"
aliases: ["Control from other programs"]
tags: [kinovea, type/permanent, kinovea/advanced]
up: "[[12 Advanced]]"
source: official-manual
---

# Control from other programs

While a Kinovea window is running it is possible to send it commands from a third party program or script. As an example this can be used to trigger recording based on a software event.

The commands use the Windows messaging system with the **WM_COPYDATA** message. The exact way to create these Windows messages depends on the programming language or platform used to write the third party application. Each command has to be sent separately. There is no return value.

The general format of the messages is the following:

```
Kinovea:<Category>.<Command>
```

The list of categories and commands is available under **Options ‣ Preferences ‣ Keyboard**.

For example:

```
Kinovea:CaptureScreen.ToggleRecording

Kinovea:PlayerScreen.TogglePlay
```

> [!tip]
> Kinovea windows continue to receive messages when minimized and not in the foreground. If there are multiple windows opened you need to send the message to the correct window based on its title.

---
⬆ [[12 Advanced]] · ⬅ [[12d Command line options]]
