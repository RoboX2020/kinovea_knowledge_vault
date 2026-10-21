---
id: "8e3"
title: "Export data to spreadsheet"
aliases: ["Export data to spreadsheet"]
tags: [kinovea, type/permanent, kinovea/export]
up: "[[8e Exporting spreadsheet documents]]"
source: official-manual
---

# Export data to spreadsheet

Another option to export data is to use the converters menus under **File ‣ Export to spreadsheet**.

The following options are available:

- **LibreOffice (.odf)**

- **Microsoft Excel (.xml)**

- **Web (.html)**

- **Gnuplot (.txt)**

The underlying mechanism for these menus is to **convert** the annotation data into the output format: it does not perform any higher level computations. This approach has the following differences with the export from the kinematics dialogs:

- The coordinates do not use filtering.

- Only the coordinates are exported, not any higher level measurements like speed or acceleration.

- Each object is exported independently in its own table.

- Key images times are exported.

- Stopwatches are exported.

- The time column uses the configured timecode format and may not be numerical in nature.

To use Gnuplot to plot the trajectory data on a 3D graph with time as the third dimensions, you can use the following commands:

```
gnuplot> set xlabel "Time"
gnuplot> set ylabel "X-AXIS"
gnuplot> set zlabel "Y-AXIS"
gnuplot> set ticslevel 0
gnuplot> splot "weightlift.txt" using 1:2:3 with lines
```

![[gnuplot.png]]

---
⬆ [[8e Exporting spreadsheet documents]] · ⬅ [[8e2 Export measurements from kinematics dialogs]] · ➡ [[8e4 Citation examples]]
