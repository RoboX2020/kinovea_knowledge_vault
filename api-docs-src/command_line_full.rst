Command line reference (complete)
=================================

.. note:: This chapter is not part of the official Kinovea manual. It was compiled from the Kinovea source code (github.com/Kinovea/Kinovea, commit ``13d0236``, October 2026) to document behavior the manual omits. Where the official manual and the source disagree, the source is what actually runs.

This supersedes the *Command line options* chapter, which omits several options.

.. code-block:: text

    kinovea.exe [-name <string>] [-id <string>] [-video <path>] [-speed <1..1000>]
                [-video2 <path>] [-stretch] [-hideExplorer]
    kinovea.exe <file>
    kinovea.exe -help | -h

Options
-------

.. list-table::
    :header-rows: 1
    :widths: 22 78

    * - Option
      - Meaning
    * - ``-name <string>``
      - Restore the saved window with this name. Takes precedence over every other option: if present, ``-video`` etc. are ignored.
    * - ``-id <string>``
      - Restore the saved window with this id. Used internally; checked after ``-name``.
    * - ``-video <path>``
      - Load and **autoplay** this video in a player screen.
    * - ``-video2 <path>``
      - *Undocumented in the manual.* Load a second video in a second player screen (dual mode). Requires ``-video``.
    * - ``-speed <n>``
      - Playback speed as a percentage of the original frame rate, applied to both videos. The manual says ``0..200``; the code actually clamps to **1–1000**. Unparseable values fall back to 100. Use ``.`` as decimal separator.
    * - ``-stretch``
      - Expand the video(s) to fit the screen.
    * - ``-hideExplorer``
      - Hide the navigation pane.
    * - ``<file>`` (sole argument)
      - *Undocumented.* If the only argument is an existing file, it is opened in a single player with autoplay **and stretch**. This is what happens when a file is dropped on ``kinovea.exe``.
    * - ``-help``, ``-h``
      - *Undocumented.* Print usage to the parent console.

Notes
-----

* ``-speed``, ``-video2``, ``-stretch`` and ``-hideExplorer`` without ``-video`` are ignored with a logged error.
* Examples:

.. code-block:: text

    kinovea.exe -name "Dual replay"
    kinovea.exe -video "C:\clips\jump.mp4" -speed 25 -stretch
    kinovea.exe -video "a.mp4" -video2 "b.mp4" -hideExplorer
