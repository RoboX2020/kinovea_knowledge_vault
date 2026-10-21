KVA file format reference
=========================

.. note:: This chapter is not part of the official Kinovea manual. It was compiled from the Kinovea source code (github.com/Kinovea/Kinovea, commit ``13d0236``, October 2026) to document behavior the manual omits. Where the official manual and the source disagree, the source is what actually runs.

KVA files are UTF-8 XML. The current Kinovea writes **FormatVersion 2.1**.

.. warning::
    The XML schemas in the Kinovea repository (``Tools/XML/Schema/kva.2.0.xsd`` and ``drawings.xsd``) are badly outdated: they describe a ``CalibrationHelp`` element that is no longer written and lack most current sections (coordinate system, trackability, camera motion, video filters…). Do not validate against them. Treat the structure below, taken from the serializer, as authoritative, and read files leniently: Kinovea itself skips unknown elements.

Root element and section order
------------------------------

The root is ``<KinoveaVideoAnalysis>``. Children are written in this order; sections are omitted when empty:

.. list-table::
    :header-rows: 1
    :widths: 30 70

    * - Element
      - Content
    * - ``FormatVersion``
      - ``2.1``
    * - ``Producer``
      - ``Kinovea.<version>``
    * - ``OriginalFilename``, ``FullPath``, ``ByteLength``
      - Source video name (no extension), full path, size in bytes. Absent for capture recordings.
    * - ``CaptureRecording``
      - ``true`` for KVAs written alongside a capture recording (replaces the three elements above).
    * - ``GlobalTitle``
      - Optional title.
    * - ``ImageSize``
      - ``width;height`` in pixels.
    * - ``Aspect``, ``Rotation``, ``Mirror``, ``Demosaicing``, ``Deinterlacing``
      - Image-level overrides.
    * - ``StabilizationTrack``
      - Id of the track used for stabilization.
    * - ``BackgroundColor``
      - Background layer color.
    * - ``AverageTimeStampsPerFrame``
      - Timestamps per frame in the video's time base.
    * - ``CaptureFramerate``, ``VideoFramerate``
      - Real capture fps (high-speed calibration) and file playback fps. Invariant culture (``.`` decimal).
    * - ``FirstTimeStamp``, ``SelectionStart``, ``SelectionEnd``
      - Timestamps of the first frame and working zone. Absent for capture recordings.
    * - ``TimeOrigin``
      - Timestamp of the custom time origin.
    * - ``Context``
      - Context variables string, if any.
    * - ``Calibration``
      - Spatial calibration (line or plane), lens distortion.
    * - ``Keyframes``
      - ``<Keyframe>`` elements, each with its position, title, color, comments and ``<Drawings>``.
    * - ``Chronos``
      - ``<Chrono>``, ``<ChronoMulti>`` and ``<Counter>`` elements (attributes ``id``, ``name``).
    * - ``Tracks``
      - ``<Track>`` elements (trajectory objects).
    * - ``Spotlights``, ``NumberSequence``
      - Singleton spotlight and auto-numbers drawings.
    * - ``CoordinateSystem``
      - Coordinate system object.
    * - ``TestGrid``
      - Test grid (lens calibration helper).
    * - ``Trackability``
      - Tracking timelines for every trackable drawing point.
    * - ``VideoFilters``
      - Kinogram and other filter configurations.
    * - ``CameraMotion``
      - Camera motion estimation data.

Which sections are written depends on the export flags: *Calibration* (``Calibration``, ``CoordinateSystem``), *Drawings* (``Keyframes``, ``TestGrid``) and *VideoSpecific* (``Chronos``, ``Tracks``, ``Spotlights``, ``NumberSequence``, ``Trackability``, ``VideoFilters``, ``CameraMotion``). A full save sets all three.

Conventions
-----------

* Points are written as ``x;y``; sizes as ``w;h``.
* Times are stored as **timestamps** in the video's own time base, not milliseconds. Convert with ``AverageTimeStampsPerFrame`` and ``VideoFramerate``; ``TimeOrigin`` gives the zero.
* Numbers use the invariant culture regardless of the user's locale.
* Older files (1.x, 2.0) are upgraded on load; the repository ships XSLT converters in ``Tools/XML/Kva to Kva/``.

Practical advice
----------------

To produce KVA files programmatically, create the annotations once in Kinovea, save, and use that file as a template. That is far more reliable than writing from scratch against an incomplete specification. For reading measurement data, the spreadsheet exports (see *Export*) are usually easier than parsing KVA.
