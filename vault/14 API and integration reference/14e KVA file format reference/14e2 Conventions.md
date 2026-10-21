---
id: "14e2"
title: "Conventions"
aliases: ["Conventions"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14e KVA file format reference]]"
source: kinovea-source-code
---

# Conventions

- Points are written as `x;y`; sizes as `w;h`.

- Times are stored as **timestamps** in the video’s own time base, not milliseconds. Convert with `AverageTimeStampsPerFrame` and `VideoFramerate`; `TimeOrigin` gives the zero.

- Numbers use the invariant culture regardless of the user’s locale.

- Older files (1.x, 2.0) are upgraded on load; the repository ships XSLT converters in `Tools/XML/Kva to Kva/`.

---
⬆ [[14e KVA file format reference]] · ⬅ [[14e1 Root element and section order]] · ➡ [[14e3 Practical advice]]
