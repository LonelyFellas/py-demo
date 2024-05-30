import tkinter as tk
import ttkbootstrap as ttkb
from tkinter import messagebox
import subprocess
import time
import win32gui
import win32con
from windows.keyevent import on_power, on_portrait, on_landscape, on_screencap, on_back_navigate, on_task_manage, \
    on_volume_up, \
    on_volume_down, on_volume_close, on_main_menu, on_key_press, on_install_apk


def find_window_by_title(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        raise Exception(f"Window with title '{title}' not found!")
    return hwnd


def embed_window(parent_hwnd, child_hwnd):
    win32gui.SetParent(child_hwnd, parent_hwnd)
    win32gui.SetWindowLong(child_hwnd, win32con.GWL_STYLE, win32con.WS_VISIBLE | win32con.WS_CHILD)
    win32gui.SetWindowPos(child_hwnd, None, 0, 0, 340, 600, win32con.SWP_NOZORDER | win32con.SWP_NOACTIVATE)
    # win32gui.SetFocus(child_hwnd)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


# 启动 scrcpy 或其他你想嵌入的程序
scrcpy_process = subprocess.Popen(['scrcpy', '-s', '192.168.1.2:5555'])

# 给程序一点时间启动并创建窗口
time.sleep(5)

# 找到 scrcpy 窗口
try:
    scrcpy_hwnd = find_window_by_title("redroid12_arm64")
except Exception as e:
    print(e)
    scrcpy_process.terminate()
    exit(1)

# 创建主窗口
# root = tk.Tk()
root = ttkb.Window(themename="litera")
root.title("redroid12_arm64")
root.geometry("400x600")
root.protocol("WM_DELETE_WINDOW", on_closing)
# root.resizable(False, False)

# 嵌入 scrcpy 窗口
embed_window(root.winfo_id(), scrcpy_hwnd)


def on_close():
    print("Window closed")
    root.destroy()


# 绑定按键按下事件
root.bind("<KeyPress>", on_key_press)
# 绑定窗口关闭事件
root.protocol("WM_DELETE_WINDOW", on_close)

frame = ttkb.Frame(root)
frame.pack(pady=20)

button1 = ttkb.Button(frame, text="音量+", command=on_volume_up, )
button2 = ttkb.Button(frame, text="音量-", command=on_volume_down)
button3 = ttkb.Button(frame, text="静音", command=on_volume_close)
button4 = ttkb.Button(frame, text="主界面", command=on_main_menu)
button5 = ttkb.Button(frame, text="返回", command=on_back_navigate)
button6 = ttkb.Button(frame, text="电源", command=on_power)
button7 = ttkb.Button(frame, text="任务管理", command=on_task_manage)
button8 = ttkb.Button(frame, text="横屏", command=on_landscape)
button9 = ttkb.Button(frame, text="竖屏", command=on_portrait)
button10 = ttkb.Button(frame, text="截屏", command=on_screencap)
button11 = ttkb.Button(frame, text="安装apk", command=lambda: on_install_apk(root))

# 使用 pack 方法将按钮放置在右上角
button1.place(x=440, y=0)
button2.place(x=440, y=30)
button3.place(x=440, y=60)
button4.place(x=440, y=90)
button5.place(x=440, y=120)
button6.place(x=440, y=150)
button7.place(x=440, y=180)
button8.place(x=440, y=210)
button9.place(x=440, y=240)
button10.place(x=440, y=270)
button11.place(x=440, y=300)

root.mainloop()
