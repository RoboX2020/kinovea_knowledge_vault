---
id: "14f"
title: "Custom posture tool format"
aliases: ["Custom posture tool format"]
tags: [kinovea, type/structure, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14 API and integration reference]]"
source: kinovea-source-code
---

# Custom posture tool format

> [!note]
> This chapter is not part of the official Kinovea manual. It was compiled from the Kinovea source code (github.com/Kinovea/Kinovea, commit `13d0236`, October 2026) to document behavior the manual omits. Where the official manual and the source disagree, the source is what actually runs.

Every tool in the *Posture* menu (goniometer, human model, bike fit, OpenPose body 25, etc.) is an XML file. You can create your own: drop a new `.xml` file into `<Kinovea install dir>\DrawingTools\Custom\` and restart Kinovea. Only files with the `.xml` extension are loaded. The shipped files are the best examples; this chapter documents the vocabulary their parser understands.

## Notes in this chapter

- [[14f1 Minimal skeleton]] — Id must be a unique GUID: it is how KVA files refer back to the tool.
- [[14f2 Real example- the shipped Goniometer]]
- [[14f3 Data section]]
- [[14f4 Interaction section]] — Handles/Handle makes something draggable.
- [[14f5 Variables section]]
- [[14f6 Menus and extras]]
- [[14f7 Tips]]

---
⬆ [[14 API and integration reference]] · ⬅ [[14e KVA file format reference]]
