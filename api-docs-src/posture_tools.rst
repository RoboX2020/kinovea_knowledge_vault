Custom posture tool format
==========================

.. note:: This chapter is not part of the official Kinovea manual. It was compiled from the Kinovea source code (github.com/Kinovea/Kinovea, commit ``13d0236``, October 2026) to document behavior the manual omits. Where the official manual and the source disagree, the source is what actually runs.

Every tool in the *Posture* menu (goniometer, human model, bike fit, OpenPose body 25, etc.) is an XML file. You can create your own: drop a new ``.xml`` file into ``<Kinovea install dir>\DrawingTools\Custom\`` and restart Kinovea. Only files with the ``.xml`` extension are loaded. The shipped files are the best examples; this chapter documents the vocabulary their parser understands.

Minimal skeleton
----------------

.. code-block:: xml

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

``Id`` must be a unique GUID: it is how KVA files refer back to the tool. Points are referenced everywhere by **zero-based index** in ``<Points>``. ``DisplayName`` may be a localization key (e.g. ``DrawingName_Goniometer``) or plain text.

Real example: the shipped Goniometer
------------------------------------

.. code-block:: xml

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

Data section
------------

.. list-table::
    :header-rows: 1
    :widths: 22 78

    * - Element
      - Attributes
    * - ``Points/Point``
      - ``value="x;y"`` initial position; ``name``, ``color``. (Legacy 1.0 files use ``InitialConfiguration/Point`` with text content, and ``PointCount``, which is ignored.)
    * - ``Segments/Segment``
      - ``point1``, ``point2``; ``name``, ``style`` (``Solid`` | ``Dash``), ``width``, ``color``, ``arrowBegin`` / ``arrowEnd`` (``arrowStart`` also accepted), ``optionGroup``.
    * - ``Circles/Circle`` (alias ``Ellipses``)
      - ``center`` (point index), ``radius``, ``style``, ``width``, ``color``, ``name``, ``optionGroup``.
    * - ``Angles/Angle``
      - ``origin``, ``leg1``, ``leg2``; ``signed``, ``ccw``, ``supplementary``, ``radius`` (negative = inside), ``textDistance``, ``tenth`` (one decimal), ``symbol``, ``color``, ``name``, ``optionGroup``.
    * - ``Polylines/Polyline``
      - ``points="0;1;2;3"``; ``style``, ``width``, ``color``, ``arrowBegin``/``arrowEnd``, ``name``, ``optionGroup``.

Interaction section
-------------------

``Handles/Handle`` makes something draggable. Attributes: ``type`` (``Point`` | ``Segment`` | ``Circle`` | ``Ellipse``), ``reference`` (index of the point/segment/circle), ``trackable`` (included in tracking), ``color``, ``name``, ``optionGroup``.

A handle may contain one **constraint** (where it is allowed to go) and **impacts** (what else moves when it moves).

``Constraint`` takes ``type`` and an optional ``optionGroup``, and a child element carrying that type's parameters:

.. list-table::
    :header-rows: 1
    :widths: 26 74

    * - Constraint type
      - Parameters / meaning
    * - ``None``
      - Free movement.
    * - ``LineSlide``
      - ``point1``, ``point2``, ``position`` — slide along the line through two points.
    * - ``VerticalSlide`` / ``HorizontalSlide``
      - Move only vertically / horizontally.
    * - ``DistanceToPoint``
      - ``point`` — keep a fixed distance (move on a circle).
    * - ``RotationSteps``
      - ``origin``, ``leg1``, ``step`` (degrees), ``keepDistance`` — snap rotation to steps.
    * - ``PerpendicularSlide``
      - ``origin``, ``leg1`` — slide perpendicular to a leg.
    * - ``ParallelSlide``
      - ``a``, ``b``, ``c`` — keep parallel to a reference segment.
    * - ``LockedInPlace``
      - Cannot be moved.

``Impacts`` (or ``Impact``) contains any of:

.. list-table::
    :header-rows: 1
    :widths: 30 70

    * - Impact element
      - Parameters / meaning
    * - ``Align``
      - ``point1``, ``point2``, ``pointToAlign`` — keep a point on a line.
    * - ``VerticalAlign`` / ``HorizontalAlign``
      - ``point`` — keep a point vertically / horizontally aligned with the handle.
    * - ``Pivot``
      - ``pivot``, ``impacted`` — rotate other points around a pivot.
    * - ``KeepAngle``
      - ``origin``, ``leg1``, ``leg2`` — preserve an angle.
    * - ``HorizontalSymmetry``
      - ``axis``, ``impacting``, ``impacted`` — mirror a point across an axis.
    * - ``SegmentCenter``
      - ``point1``, ``point2``, ``pointToMove`` — keep a point at a segment's midpoint.
    * - ``PerdpendicularAlign``
      - ``origin``, ``leg1``, ``pointToMove``. **Note the misspelling**: the parser expects ``PerdpendicularAlign``. The correct spelling is silently ignored.
    * - ``ParallelAlign``
      - ``a``, ``b``, ``c``, ``pointToMove``.

``HitZone/Polygon points="2;11;15;6"`` defines an area; dragging inside it moves the whole drawing.

Variables section
-----------------

* ``Distances/Distance point1 point2`` — display a measured distance; ``symbol``, ``color``, ``name``, ``optionGroup``.
* ``Positions/Position point`` — display coordinates of a point; ``symbol``, ``color``, ``optionGroup``.
* ``ComputedPoints/ComputedPoint`` — a weighted point, e.g. center of mass. Nest ``ComputedPoint`` (with ``weight``) and ``ReferencePoint ref="<index>" weight="…"`` arbitrarily deep; ``name``, ``color``, ``symbol``, ``displayCoordinates``, ``optionGroup``. Computed points are referenced elsewhere with a ``$`` prefix (``point="$0"`` = first computed point). See *10 - Human model.xml* for a full anthropometric center-of-mass model.

Menus and extras
----------------

* ``optionGroup`` on any element links it to a context-menu toggle; the element is drawn only when the option is on. Combine several with ``|`` (``optionGroup="a|b"``): **all** must be on (AND logic).
* Options are created **automatically** from every ``optionGroup`` value, labelled with that value and **off by default**. That's how *Human model* gets its "Display knee angles" toggles without declaring anything.
* ``Options/Option key label default hidden`` declares an option explicitly, to set a friendlier ``label``, make it ``default="true"``, or keep it out of the menu with ``hidden="true"`` (used by the OpenPose model).
* ``Capabilities flipHorizontal flipVertical`` — adds Flip menu items. Must be an empty element.
* ``TrackingParameters`` — per-tool tracking parameter overrides.

Tips
----

* Start from the shipped file closest to what you want. Change the ``Id``.
* Kinovea logs and skips unknown elements rather than failing, so a typo silently does nothing. Check ``%APPDATA%\Kinovea\Logs\log.txt`` (``log.<window>.txt`` for named windows; portable installs keep settings and logs next to the exe) if something doesn't appear.
