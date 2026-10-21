---
id: "14b4"
title: "Example- C-"
aliases: ["Example- C-"]
tags: [kinovea, type/permanent, kinovea/api-and-integration-reference, source/code-derived]
up: "[[14b Remote control command reference]]"
source: kinovea-source-code
---

# Example- C-

```csharp
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
```

---
⬆ [[14b Remote control command reference]] · ⬅ [[14b3 Example- Python (ctypes)]] · ➡ [[14b5 PlayerScreen commands]]
