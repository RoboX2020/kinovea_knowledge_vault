---
id: "14e1"
title: "Root element and section order"
aliases: ["Root element and section order"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14e KVA file format reference]]"
source: kinovea-source-code
---

# Root element and section order

The root is `<KinoveaVideoAnalysis>`. Children are written in this order; sections are omitted when empty:

| Element                                                        | Content                                                                                           |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| `FormatVersion`                                                | `2.1`                                                                                             |
| `Producer`                                                     | `Kinovea.<version>`                                                                               |
| `OriginalFilename`, `FullPath`, `ByteLength`                   | Source video name (no extension), full path, size in bytes. Absent for capture recordings.        |
| `CaptureRecording`                                             | `true` for KVAs written alongside a capture recording (replaces the three elements above).        |
| `GlobalTitle`                                                  | Optional title.                                                                                   |
| `ImageSize`                                                    | `width;height` in pixels.                                                                         |
| `Aspect`, `Rotation`, `Mirror`, `Demosaicing`, `Deinterlacing` | Image-level overrides.                                                                            |
| `StabilizationTrack`                                           | Id of the track used for stabilization.                                                           |
| `BackgroundColor`                                              | Background layer color.                                                                           |
| `AverageTimeStampsPerFrame`                                    | Timestamps per frame in the video’s time base.                                                    |
| `CaptureFramerate`, `VideoFramerate`                           | Real capture fps (high-speed calibration) and file playback fps. Invariant culture (`.` decimal). |
| `FirstTimeStamp`, `SelectionStart`, `SelectionEnd`             | Timestamps of the first frame and working zone. Absent for capture recordings.                    |
| `TimeOrigin`                                                   | Timestamp of the custom time origin.                                                              |
| `Context`                                                      | Context variables string, if any.                                                                 |
| `Calibration`                                                  | Spatial calibration (line or plane), lens distortion.                                             |
| `Keyframes`                                                    | `<Keyframe>` elements, each with its position, title, color, comments and `<Drawings>`.           |
| `Chronos`                                                      | `<Chrono>`, `<ChronoMulti>` and `<Counter>` elements (attributes `id`, `name`).                   |
| `Tracks`                                                       | `<Track>` elements (trajectory objects).                                                          |
| `Spotlights`, `NumberSequence`                                 | Singleton spotlight and auto-numbers drawings.                                                    |
| `CoordinateSystem`                                             | Coordinate system object.                                                                         |
| `TestGrid`                                                     | Test grid (lens calibration helper).                                                              |
| `Trackability`                                                 | Tracking timelines for every trackable drawing point.                                             |
| `VideoFilters`                                                 | Kinogram and other filter configurations.                                                         |
| `CameraMotion`                                                 | Camera motion estimation data.                                                                    |

Which sections are written depends on the export flags: *Calibration* (`Calibration`, `CoordinateSystem`), *Drawings* (`Keyframes`, `TestGrid`) and *VideoSpecific* (`Chronos`, `Tracks`, `Spotlights`, `NumberSequence`, `Trackability`, `VideoFilters`, `CameraMotion`). A full save sets all three.

---
⬆ [[14e KVA file format reference]] · ➡ [[14e2 Conventions]]
