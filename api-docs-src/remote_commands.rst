Remote control command reference
================================

.. note:: This chapter is not part of the official Kinovea manual. It was compiled from the Kinovea source code (github.com/Kinovea/Kinovea, commit ``13d0236``, October 2026) to document behavior the manual omits. Where the official manual and the source disagree, the source is what actually runs.

The official manual explains that commands can be sent through ``WM_COPYDATA`` but defers the command list to the Keyboard preferences page inside the application. This chapter is that list, plus the exact wire protocol.

Protocol
--------

* **Message:** ``WM_COPYDATA`` (``0x004A``) sent with ``SendMessage`` to the Kinovea main window.
* **dwData:** must be ``0``. Any other value is rejected as malformed.
* **lpData / cbData:** the command string, NUL-terminated. Both UTF-16 (wide) and ANSI encodings are accepted: Kinovea tries UTF-16 first, then ANSI.
* **Format:** ``Kinovea:<Category>.<Command>``. Everything before the first ``:`` must be ``Kinovea``; the payload must split into exactly two non-empty tokens on ``.``.
* **Categories:** only ``PlayerScreen``, ``CaptureScreen`` and ``Window`` are dispatched. Other category names shown in the Keyboard preferences (``FileExplorer``, ``ThumbnailViewer…``, ``DualPlayer``, ``DualCapture``) are hotkey-only and **cannot** be triggered remotely.
* **Names are case-sensitive** (parsed with ``Enum.TryParse`` without ignore-case). ``toggleplay`` fails; ``TogglePlay`` works.
* **Fan-out:** a ``PlayerScreen`` command is executed on *every* open player screen; a ``CaptureScreen`` command on *every* capture screen. There is no way to target only the left or right screen.
* **No reply.** ``SendMessage`` returns when the message is handled, but no status is returned. Failures appear only in Kinovea's log file.
* **Minimized windows** still receive and execute commands. Kinovea explicitly allows ``WM_COPYDATA`` through UIPI (``ChangeWindowMessageFilterEx``), so a non-elevated sender can talk to an elevated Kinovea.

Finding the window
------------------

Each Kinovea window's title is ``Kinovea [<name>]``, where ``<name>`` is the window name set in :menuselection:`Window --> Window properties…`, or a name derived from its id if none was set. Locate it with ``FindWindow(NULL, "Kinovea [Replay]")``. Naming your windows makes scripting much easier.

Example: Python (ctypes)
------------------------

.. code-block:: python

    import ctypes
    from ctypes import wintypes

    WM_COPYDATA = 0x004A

    class COPYDATASTRUCT(ctypes.Structure):
        _fields_ = [("dwData", ctypes.c_size_t),
                    ("cbData", wintypes.DWORD),
                    ("lpData", ctypes.c_void_p)]

    def send(command, window_title="Kinovea [Replay]"):
        hwnd = ctypes.windll.user32.FindWindowW(None, window_title)
        if not hwnd:
            raise RuntimeError("Kinovea window not found: " + window_title)
        buf = ctypes.create_unicode_buffer("Kinovea:" + command)   # UTF-16, NUL-terminated
        cds = COPYDATASTRUCT(0, ctypes.sizeof(buf), ctypes.cast(buf, ctypes.c_void_p))
        ctypes.windll.user32.SendMessageW(hwnd, WM_COPYDATA, 0, ctypes.byref(cds))

    send("CaptureScreen.ToggleRecording")

Example: C#
-----------

.. code-block:: csharp

    [StructLayout(LayoutKind.Sequential)]
    struct COPYDATASTRUCT { public IntPtr dwData; public int cbData; public IntPtr lpData; }

    [DllImport("user32.dll", CharSet = CharSet.Unicode)] static extern IntPtr FindWindow(string cls, string title);
    [DllImport("user32.dll")] static extern IntPtr SendMessage(IntPtr hWnd, int msg, IntPtr wParam, ref COPYDATASTRUCT cds);

    static void Send(string command, string title = "Kinovea [Replay]")
    {
        IntPtr hwnd = FindWindow(null, title);
        string msg = "Kinovea:" + command + "\0";
        var cds = new COPYDATASTRUCT { dwData = IntPtr.Zero, cbData = msg.Length * 2, lpData = Marshal.StringToHGlobalUni(msg) };
        SendMessage(hwnd, 0x004A, IntPtr.Zero, ref cds);
        Marshal.FreeHGlobal(cds.lpData);
    }

PlayerScreen commands
---------------------

Default keys are the factory hotkeys; users can rebind them, but remote commands are addressed by name, so rebinding does not affect them.

.. list-table::
    :header-rows: 1
    :widths: 50 15 35

    * - Message
      - Default key
      - Effect
    * - ``Kinovea:PlayerScreen.ResetViewport``
      - Esc
      - Reset the viewport (exit zoom, close menus).
    * - ``Kinovea:PlayerScreen.Close``
      - Ctrl + F4
      - Close the screen.
    * - ``Kinovea:PlayerScreen.TogglePlay``
      - Space
      - Start/stop playback.
    * - ``Kinovea:PlayerScreen.IncreaseSpeed10``
      - Up
      - Increase playback speed by 10%.
    * - ``Kinovea:PlayerScreen.DecreaseSpeed10``
      - Down
      - Decrease playback speed by 10%.
    * - ``Kinovea:PlayerScreen.IncreaseSpeed1``
      - Shift + Up
      - Increase playback speed by 1%.
    * - ``Kinovea:PlayerScreen.DecreaseSpeed1``
      - Shift + Down
      - Decrease playback speed by 1%.
    * - ``Kinovea:PlayerScreen.GotoPreviousImage``
      - Left
      - Step one frame backward.
    * - ``Kinovea:PlayerScreen.GotoNextImage``
      - Right
      - Step one frame forward.
    * - ``Kinovea:PlayerScreen.GotoFirstImage``
      - Home
      - Go to the first frame.
    * - ``Kinovea:PlayerScreen.GotoLastImage``
      - End
      - Go to the last frame.
    * - ``Kinovea:PlayerScreen.GotoPreviousImageForceLoop``
      - Shift + Left
      - Step backward, wrapping to the end at the start.
    * - ``Kinovea:PlayerScreen.LargeJumpBackward``
      - Page Up
      - Large jump backward.
    * - ``Kinovea:PlayerScreen.LargeJumpForward``
      - Page Down
      - Large jump forward.
    * - ``Kinovea:PlayerScreen.SmallJumpBackward``
      - Shift + Page Up
      - Small jump backward.
    * - ``Kinovea:PlayerScreen.SmallJumpForward``
      - Shift + Page Down
      - Small jump forward.
    * - ``Kinovea:PlayerScreen.GotoPreviousKeyframe``
      - Ctrl + Left
      - Go to the previous key image.
    * - ``Kinovea:PlayerScreen.GotoNextKeyframe``
      - Ctrl + Right
      - Go to the next key image.
    * - ``Kinovea:PlayerScreen.GotoSyncPoint``
      - F8
      - Go to the synchronization point.
    * - ``Kinovea:PlayerScreen.IncreaseSyncAlpha``
      - Alt + Num +
      - Increase merge opacity in dual mode.
    * - ``Kinovea:PlayerScreen.DecreaseSyncAlpha``
      - Alt + Num −
      - Decrease merge opacity in dual mode.
    * - ``Kinovea:PlayerScreen.ToggleSyncMerge``
      - F9
      - **No effect via remote control.** The player screen has no handler for it; superposition is handled by the dual-player controller, which external messages do not reach.
    * - ``Kinovea:PlayerScreen.IncreaseZoom``
      - Ctrl + Num +
      - Zoom in.
    * - ``Kinovea:PlayerScreen.DecreaseZoom``
      - Ctrl + Num −
      - Zoom out.
    * - ``Kinovea:PlayerScreen.ResetZoom``
      - Ctrl + Num 0
      - Reset zoom.
    * - ``Kinovea:PlayerScreen.AddKeyframe``
      - Ins
      - Add a key image at the current frame.
    * - ``Kinovea:PlayerScreen.DeleteKeyframe``
      - Ctrl + Del
      - Delete the key image at the current frame.
    * - ``Kinovea:PlayerScreen.Preset1``
      - Ctrl + Num 1
      - Apply key image preset 1.
    * - ``Kinovea:PlayerScreen.Preset2``
      - Ctrl + Num 2
      - Apply key image preset 2.
    * - ``Kinovea:PlayerScreen.Preset3``
      - Ctrl + Num 3
      - Apply key image preset 3.
    * - ``Kinovea:PlayerScreen.Preset4``
      - Ctrl + Num 4
      - Apply key image preset 4.
    * - ``Kinovea:PlayerScreen.Preset5``
      - Ctrl + Num 5
      - Apply key image preset 5.
    * - ``Kinovea:PlayerScreen.Preset6``
      - Ctrl + Num 6
      - Apply key image preset 6.
    * - ``Kinovea:PlayerScreen.Preset7``
      - Ctrl + Num 7
      - Apply key image preset 7.
    * - ``Kinovea:PlayerScreen.Preset8``
      - Ctrl + Num 8
      - Apply key image preset 8.
    * - ``Kinovea:PlayerScreen.Preset9``
      - Ctrl + Num 9
      - Apply key image preset 9.
    * - ``Kinovea:PlayerScreen.Preset10``
      - —
      - Apply key image preset 10.
    * - ``Kinovea:PlayerScreen.CutDrawing``
      - Ctrl + X
      - Cut the selected drawing.
    * - ``Kinovea:PlayerScreen.CopyDrawing``
      - Ctrl + C
      - Copy the selected drawing.
    * - ``Kinovea:PlayerScreen.PasteDrawing``
      - Ctrl + V
      - Paste drawing at the mouse position.
    * - ``Kinovea:PlayerScreen.PasteInPlaceDrawing``
      - —
      - Paste drawing at its original position.
    * - ``Kinovea:PlayerScreen.DeleteDrawing``
      - Del
      - Delete the selected drawing.
    * - ``Kinovea:PlayerScreen.ValidateDrawing``
      - Enter
      - Finish the drawing in progress.
    * - ``Kinovea:PlayerScreen.CopyImage``
      - Ctrl + Shift + C
      - Copy the current image to the clipboard.
    * - ``Kinovea:PlayerScreen.CopyTime``
      - —
      - Copy the current time to the clipboard.
    * - ``Kinovea:PlayerScreen.ToggleDrawingsVisibility``
      - —
      - Show/hide all drawings.
    * - ``Kinovea:PlayerScreen.ChronometerStartStop``
      - F5
      - Start/stop the active stopwatch.
    * - ``Kinovea:PlayerScreen.ChronometerSplit``
      - F6
      - Record a split on the active stopwatch.
    * - ``Kinovea:PlayerScreen.CadenceBeat``
      - F7
      - Add a beat to the cadence counter.
    * - ``Kinovea:PlayerScreen.StartAllTracking``
      - —
      - Start tracking for all trackable drawings.

CaptureScreen commands
----------------------

.. list-table::
    :header-rows: 1
    :widths: 50 15 35

    * - Message
      - Default key
      - Effect
    * - ``Kinovea:CaptureScreen.ResetViewport``
      - Esc
      - Reset the viewport (exit zoom, close menus).
    * - ``Kinovea:CaptureScreen.OpenConfiguration``
      - F12
      - Open the camera configuration dialog.
    * - ``Kinovea:CaptureScreen.Close``
      - Ctrl + F4
      - Close the screen.
    * - ``Kinovea:CaptureScreen.ToggleGrabbing``
      - Space
      - Pause/resume the camera stream.
    * - ``Kinovea:CaptureScreen.ToggleRecording``
      - Ctrl + Enter
      - Start/stop recording.
    * - ``Kinovea:CaptureScreen.TakeSnapshot``
      - Shift + Enter
      - Save a snapshot image.
    * - ``Kinovea:CaptureScreen.ToggleArmCaptureTrigger``
      - —
      - Arm/disarm the capture trigger.
    * - ``Kinovea:CaptureScreen.IncreaseZoom``
      - —
      - Zoom in.
    * - ``Kinovea:CaptureScreen.DecreaseZoom``
      - —
      - Zoom out.
    * - ``Kinovea:CaptureScreen.ResetZoom``
      - —
      - Reset zoom.
    * - ``Kinovea:CaptureScreen.GotoPreviousImage``
      - Left
      - Step one frame backward.
    * - ``Kinovea:CaptureScreen.GotoNextImage``
      - Right
      - Step one frame forward.
    * - ``Kinovea:CaptureScreen.GotoFirstImage``
      - Home
      - Go to the first frame.
    * - ``Kinovea:CaptureScreen.GotoLastImage``
      - End
      - Go to the last frame.
    * - ``Kinovea:CaptureScreen.BackwardRound10Percent``
      - Page Up
      - Move back 10% in the delay buffer.
    * - ``Kinovea:CaptureScreen.ForwardRound10Percent``
      - Page Down
      - Move forward 10% in the delay buffer.
    * - ``Kinovea:CaptureScreen.BackwardRound1Percent``
      - Shift + Page Up
      - Move back 1% in the delay buffer.
    * - ``Kinovea:CaptureScreen.ForwardRound1Percent``
      - Shift + Page Down
      - Move forward 1% in the delay buffer.
    * - ``Kinovea:CaptureScreen.ToggleDelayedDisplay``
      - Alt + Home
      - Toggle the delayed display.
    * - ``Kinovea:CaptureScreen.IncreaseDelayOneSecond``
      - Up
      - Increase delay by 1 s.
    * - ``Kinovea:CaptureScreen.DecreaseDelayOneSecond``
      - Down
      - Decrease delay by 1 s.
    * - ``Kinovea:CaptureScreen.IncreaseDelayOneFrame``
      - Ctrl + Up
      - Increase delay by one frame.
    * - ``Kinovea:CaptureScreen.DecreaseDelayOneFrame``
      - Ctrl + Down
      - Decrease delay by one frame.
    * - ``Kinovea:CaptureScreen.IncreaseDelayHalfSecond``
      - Shift + Up
      - Increase delay by 0.5 s.
    * - ``Kinovea:CaptureScreen.DecreaseDelayHalfSecond``
      - Shift + Down
      - Decrease delay by 0.5 s.

Window commands
---------------

These are used internally for communication between Kinovea instances. They are listed for completeness; sending them from outside is possible but rarely useful.

.. list-table::
    :header-rows: 1
    :widths: 40 60

    * - Message
      - Effect
    * - ``Kinovea:Window.PreferencesUpdated``
      - Reload the shared preferences file from disk and refresh the UI.
    * - ``Kinovea:Window.VariableTableImported``
      - Reload context variable tables.
    * - ``Kinovea:Window.CameraUpdated``
      - Reload camera aliases/icons.
    * - ``Kinovea:Window.Close``
      - Close this window (may prompt if annotations are unsaved).
