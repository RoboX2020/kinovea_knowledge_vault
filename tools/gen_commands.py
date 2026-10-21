import re, sys
src = sys.argv[1]
enums = open(f"{src}/Kinovea.Services/Commands/CommandEnums.cs", encoding="utf-8-sig").read()
binds = open(f"{src}/Kinovea.Services/Commands/HotkeySettingsManager.cs", encoding="utf-8-sig").read()
import glob
impl = {}
for f in glob.glob(f"{src}/Kinovea.ScreenManager/**/*.cs", recursive=True):
    t = open(f, encoding="utf-8-sig", errors="ignore").read()
    for cat, name in re.findall(r'case (PlayerScreenCommands|CaptureScreenCommands)\.(\w+)', t):
        impl.setdefault(cat, set()).add(name)

KEYMAP = {"Control":"Ctrl","Add":"Num +","Subtract":"Num −","Return":"Enter","PageUp":"Page Up","PageDown":"Page Down",
          "Escape":"Esc","Insert":"Ins","Delete":"Del"}
def keyfmt(k):
    k = k.strip()
    if k == "Keys.None": return ""
    parts = [p.strip().replace("Keys.","") for p in k.split("|")]
    out = []
    for p in parts:
        m = re.match(r'NumPad(\d)', p)
        out.append(f"Num {m.group(1)}" if m else KEYMAP.get(p, p))
    return " + ".join(out)

def enum_body(name):
    m = re.search(r'enum ' + name + r'\s*\{(.*?)\n    \}', enums, re.S)
    body = m.group(1)
    items, group = [], ""
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("//") and not line.startswith("///"):
            group = line[2:].strip()
        elif re.match(r'^\w+,?$', line):
            items.append((group, line.rstrip(",")))
    return items

def bindings(enum):
    return {n: keyfmt(k) for n, k in re.findall(r'make\(' + enum + r'\.(\w+),\s*([^)]+)\)', binds)}

DESC = {
 "ResetViewport":"Reset the viewport (exit zoom, close menus).", "Close":"Close the screen.",
 "TogglePlay":"Start/stop playback.", "IncreaseSpeed10":"Increase playback speed by 10%.","DecreaseSpeed10":"Decrease playback speed by 10%.",
 "IncreaseSpeed1":"Increase playback speed by 1%.","DecreaseSpeed1":"Decrease playback speed by 1%.",
 "GotoPreviousImage":"Step one frame backward.","GotoNextImage":"Step one frame forward.","GotoFirstImage":"Go to the first frame.","GotoLastImage":"Go to the last frame.",
 "GotoPreviousImageForceLoop":"Step backward, wrapping to the end at the start.",
 "LargeJumpBackward":"Large jump backward.","LargeJumpForward":"Large jump forward.","SmallJumpBackward":"Small jump backward.","SmallJumpForward":"Small jump forward.",
 "GotoPreviousKeyframe":"Go to the previous key image.","GotoNextKeyframe":"Go to the next key image.","GotoSyncPoint":"Go to the synchronization point.",
 "IncreaseSyncAlpha":"Increase merge opacity in dual mode.","DecreaseSyncAlpha":"Decrease merge opacity in dual mode.","ToggleSyncMerge":"Toggle superposition of the two videos.",
 "IncreaseZoom":"Zoom in.","DecreaseZoom":"Zoom out.","ResetZoom":"Reset zoom.",
 "AddKeyframe":"Add a key image at the current frame.","DeleteKeyframe":"Delete the key image at the current frame.",
 "CutDrawing":"Cut the selected drawing.","CopyDrawing":"Copy the selected drawing.","PasteDrawing":"Paste drawing at the mouse position.","PasteInPlaceDrawing":"Paste drawing at its original position.",
 "DeleteDrawing":"Delete the selected drawing.","ValidateDrawing":"Finish the drawing in progress.","CopyImage":"Copy the current image to the clipboard.","CopyTime":"Copy the current time to the clipboard.",
 "ToggleDrawingsVisibility":"Show/hide all drawings.","ChronometerStartStop":"Start/stop the active stopwatch.","ChronometerSplit":"Record a split on the active stopwatch.",
 "CadenceBeat":"Add a beat to the cadence counter.","StartAllTracking":"Start tracking for all trackable drawings.",
 "OpenConfiguration":"Open the camera configuration dialog.","ToggleGrabbing":"Pause/resume the camera stream.","ToggleRecording":"Start/stop recording.",
 "TakeSnapshot":"Save a snapshot image.","ToggleArmCaptureTrigger":"Arm/disarm the capture trigger.",
 "BackwardRound10Percent":"Move back 10% in the delay buffer.","ForwardRound10Percent":"Move forward 10% in the delay buffer.",
 "BackwardRound1Percent":"Move back 1% in the delay buffer.","ForwardRound1Percent":"Move forward 1% in the delay buffer.",
 "ToggleDelayedDisplay":"Toggle the delayed display.","IncreaseDelayOneSecond":"Increase delay by 1 s.","DecreaseDelayOneSecond":"Decrease delay by 1 s.",
 "IncreaseDelayOneFrame":"Increase delay by one frame.","DecreaseDelayOneFrame":"Decrease delay by one frame.",
 "IncreaseDelayHalfSecond":"Increase delay by 0.5 s.","DecreaseDelayHalfSecond":"Decrease delay by 0.5 s.",
}
def table(cat, enum):
    items, b, im = enum_body(enum), bindings(enum), impl.get(enum, set())
    out = [".. list-table::", "    :header-rows: 1", "    :widths: 34 18 48", "", "    * - Message", "      - Default key", "      - Effect"]
    for g, n in items:
        d = DESC.get(n, "Apply key image preset %s." % n[6:] if n.startswith("Preset") else "")
        if n not in im: d = "**Not implemented** — accepted but ignored. " + d
        out += [f"    * - ``Kinovea:{cat}.{n}``", f"      - {b.get(n,'') or '—'}", f"      - {d}"]
    return "\n".join(out)

print(table("PlayerScreen","PlayerScreenCommands")); print("\n@@SPLIT@@\n"); print(table("CaptureScreen","CaptureScreenCommands"))
