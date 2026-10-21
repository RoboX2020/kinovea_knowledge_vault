---
id: "14f2"
title: "Real example- the shipped Goniometer"
aliases: ["Real example- the shipped Goniometer"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14f Custom posture tool format]]"
source: kinovea-source-code
---

# Real example- the shipped Goniometer

```xml
<Points>
  <Point value="100;100" />
  <Point value="150;100" />
  <Point value="200;100" />
  <Point value="180;70" />
</Points>
<Segments>
  <Segment name="Stationary arm" point1="0" point2="1" style="Solid" width="4"/>
  <Segment name="Reference" point1="1" point2="2" style="Dash" width="2"/>
  <Segment name="Movable arm" point1="1" point2="3" style="Solid" arrowEnd="true" width="2"/>
</Segments>
<Angles>
  <Angle origin="1" leg1="2" leg2="3" signed="true" ccw="true" supplementary="false"
         radius="-25" textDistance="40" tenth="true"/>
</Angles>
<Handles>
  <Handle type="Point" reference="0" trackable="true">
    <Impacts><KeepAngle origin="1" leg1="0" leg2="2"/></Impacts>
  </Handle>
  <Handle type="Point" reference="1" trackable="true">
    <Impacts><KeepAngle origin="1" leg1="0" leg2="2"/></Impacts>
  </Handle>
  <Handle type="Point" reference="2">
    <Constraint type="RotationSteps">
      <RotationSteps origin="1" leg1="0" step="45" keepDistance="false" />
    </Constraint>
  </Handle>
  <Handle type="Point" reference="3" trackable="true"/>
</Handles>
<Capabilities flipHorizontal="true" flipVertical="true" />
```

---
⬆ [[14f Custom posture tool format]] · ⬅ [[14f1 Minimal skeleton]] · ➡ [[14f3 Data section]]
