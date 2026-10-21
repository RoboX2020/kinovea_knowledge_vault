---
id: "14e"
title: "KVA file format reference"
aliases: ["KVA file format reference"]
tags: [kinovea, type/structure, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14 API and integration reference]]"
source: kinovea-source-code
---

# KVA file format reference

> [!note]
> This chapter is not part of the official Kinovea manual. It was compiled from the Kinovea source code (github.com/Kinovea/Kinovea, commit `13d0236`, October 2026) to document behavior the manual omits. Where the official manual and the source disagree, the source is what actually runs.

KVA files are UTF-8 XML. The current Kinovea writes **FormatVersion 2.1**.

> [!warning]
> The XML schemas in the Kinovea repository (`Tools/XML/Schema/kva.2.0.xsd` and `drawings.xsd`) are badly outdated: they describe a `CalibrationHelp` element that is no longer written and lack most current sections (coordinate system, trackability, camera motion, video filters…). Do not validate against them. Treat the structure below, taken from the serializer, as authoritative, and read files leniently: Kinovea itself skips unknown elements.

## Notes in this chapter

- [[14e1 Root element and section order]] — The root is <KinoveaVideoAnalysis>.
- [[14e2 Conventions]]
- [[14e3 Practical advice]] — To produce KVA files programmatically, create the annotations once in Kinovea, save, and use that file as a template.

---
⬆ [[14 API and integration reference]] · ⬅ [[14d Command line reference (complete)]] · ➡ [[14f Custom posture tool format]]
