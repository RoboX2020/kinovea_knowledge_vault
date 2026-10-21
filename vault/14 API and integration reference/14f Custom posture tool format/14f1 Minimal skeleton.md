---
id: "14f1"
title: "Minimal skeleton"
aliases: ["Minimal skeleton"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14f Custom posture tool format]]"
source: kinovea-source-code
---

# Minimal skeleton

```xml
<?xml version="1.0" encoding="utf-8"?>
<KinoveaPostureTool>
  <FormatVersion>1.1</FormatVersion>
  <Id>generate-a-new-guid-here</Id>
  <Name>My tool</Name>
  <DisplayName>My tool</DisplayName>
  <Icon>base64 PNG, 16×16</Icon>

  <Points>
    <Point value="100;100" />
    <Point value="200;100" />
  </Points>
  <Segments>
    <Segment point1="0" point2="1" style="Solid" width="2" />
  </Segments>
  <Handles>
    <Handle type="Point" reference="0" trackable="true" />
    <Handle type="Point" reference="1" trackable="true" />
  </Handles>
</KinoveaPostureTool>
```

`Id` must be a unique GUID: it is how KVA files refer back to the tool. Points are referenced everywhere by **zero-based index** in `<Points>`. `DisplayName` may be a localization key (e.g. `DrawingName_Goniometer`) or plain text.

---
⬆ [[14f Custom posture tool format]] · ➡ [[14f2 Real example- the shipped Goniometer]]
