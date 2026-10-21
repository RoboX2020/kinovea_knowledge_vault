---
id: "12b1"
title: "Workspace manager"
aliases: ["Workspace manager"]
tags: [kinovea, type/permanent, kinovea/advanced]
up: "[[12b Workspaces]]"
source: official-manual
---

# Workspace manager

![[workspace-manager.png]]

The workspace manager is divided in two areas. At the top, the workspace list shows the existing workspaces and lets you create, rename and delete them, or create a desktop shortcut to open a specific workspace. At the bottom, the window list shows the windows that are part of the selected workspace.

|              |                                                                                      |
|--------------|--------------------------------------------------------------------------------------|
| ![[add-16.png]] | Creates a workspace referencing the currently active windows and prompts for a name. |
| ![[rename-16.png]] | Opens a dialog to rename the selected workspace.                                     |
| ![[shortcut2.png]] | Creates a shortcut on the desktop to open the selected workspace.                    |
| ![[bin_empty.png]] | Deletes the selected workspace.                                                      |

## Creating shortcuts

To create a shortcut to open a specific workspace, use the button **Create a desktop shortcut**. (Same function as the one next to the workspace list.)

The shortcut will automatically be created on the desktop.

When the shortcut is used, Kinovea will start and reopen all the windows defined in the workspace.

![[shortcut.png]]

## Storage

Workspace files are saved as XML files in the application data folder under the Workspaces subfolder.

A workspace only contains references to windows. It does not store any state by itself.

---
⬆ [[12b Workspaces]]
