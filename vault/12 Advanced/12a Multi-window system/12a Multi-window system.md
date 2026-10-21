---
id: "12a"
title: "Multi-window system"
aliases: ["Multi-window system"]
tags: [kinovea, type/structure, kinovea/advanced]
up: "[[12 Advanced]]"
source: official-manual
---

# Multi-window system

Kinovea implements a multi-window system where each opened window (instance of Kinovea) remembers its own content and state.

Multiple instances of Kinovea can run at the same time without interfering with each other. The core preferences are shared and synchronized between instances.

You can assign names to windows to associate them with specific tasks.

> [!note]
> We use the terms “window” and “instance” interchangeably in this documentation. Each instance of Kinovea has only one main window.

This system supports many use cases, for example:

- Having a “go-to” reference video that can quickly be opened in separate window while working on other videos.

- Associating one window with a long term research project and using a separate one for quick reviews.

- Keeping a group of windows working together in a capture-and-replay workflow, and restarting them all at the same time.

> [!tip]
> It is possible to create a shortcut on the desktop to automatically open one or more specific windows, see [[12b Workspaces|Workspaces]].

## Notes in this chapter

- [[12a1 Starting new windows]] — To start a new window use the menu Window ‣ Open new window.
- [[12a2 Reopening previous windows]] — When Kinovea is started it will reopen the last window that was open when it was last closed.
- [[12a3 Window name]] — By default windows are assigned random Ids to identify them internally.
- [[12a4 Startup options]] — Each window defines startup options that are used when the window is opened.
- [[12a5 Deleting old windows]] — To delete old windows use the menu Window ‣ Window manager…, select the window to delete from the list, and click the Delete button.
- [[12a6 Global preferences vs window state]] — It can be helpful to understand what is saved in the core preferences and what is saved in the window state.

---
⬆ [[12 Advanced]] · ➡ [[12b Workspaces]]
