import subprocess
import requests
from typing import List
from datetime import datetime
import tkinter as tk
from tkinter import ttk, Wm

desktop_to_android_keycode = {
    8: 67,  # Backspace
    9: 61,  # Tab
    13: 66,  # Enter
    16: 59,  # Shift (Left)
    17: 113,  # Ctrl (Left)
    18: 57,  # Alt (Left)
    19: 121,  # Pause
    20: 115,  # Caps Lock
    27: 111,  # Escape
    32: 62,  # Space
    33: 92,  # Page Up
    34: 93,  # Page Down
    35: 123,  # End
    36: 122,  # Home
    37: 21,  # Left Arrow
    38: 19,  # Up Arrow
    39: 22,  # Right Arrow
    40: 20,  # Down Arrow
    45: 124,  # Insert
    46: 112,  # Delete
    48: 7,  # 0
    49: 8,  # 1
    50: 9,  # 2
    51: 10,  # 3
    52: 11,  # 4
    53: 12,  # 5
    54: 13,  # 6
    55: 14,  # 7
    56: 15,  # 8
    57: 16,  # 9
    65: 29,  # A
    66: 30,  # B
    67: 31,  # C
    68: 32,  # D
    69: 33,  # E
    70: 34,  # F
    71: 35,  # G
    72: 36,  # H
    73: 37,  # I
    74: 38,  # J
    75: 39,  # K
    76: 40,  # L
    77: 41,  # M
    78: 42,  # N
    79: 43,  # O
    80: 44,  # P
    81: 45,  # Q
    82: 46,  # R
    83: 47,  # S
    84: 48,  # T
    85: 49,  # U
    86: 50,  # V
    87: 51,  # W
    88: 52,  # X
    89: 53,  # Y
    90: 54,  # Z
    91: 117,  # Windows (Left)
    92: 118,  # Windows (Right)
    93: 82,  # Menu
    96: 144,  # NumPad 0
    97: 145,  # NumPad 1
    98: 146,  # NumPad 2
    99: 147,  # NumPad 3
    100: 148,  # NumPad 4
    101: 149,  # NumPad 5
    102: 150,  # NumPad 6
    103: 151,  # NumPad 7
    104: 152,  # NumPad 8
    105: 153,  # NumPad 9
    106: 155,  # NumPad *
    107: 157,  # NumPad +
    109: 156,  # NumPad -
    110: 158,  # NumPad .
    111: 154,  # NumPad /
    112: 131,  # F1
    113: 132,  # F2
    114: 133,  # F3
    115: 134,  # F4
    116: 135,  # F5
    117: 136,  # F6
    118: 137,  # F7
    119: 138,  # F8
    120: 139,  # F9
    121: 140,  # F10
    122: 141,  # F11
    123: 142,  # F12
}


def set_input_keyevent(event):
    command = ["adb", "shell", "input", "keyevent", event]
    print(command)
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(result.stderr)


def shell(cmd: List[str]):
    command = ['adb', 'shell'] + cmd
    print(command)
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def on_volume_up():
    event = "KEYCODE_VOLUME_UP"
    set_input_keyevent(event)


def on_volume_down():
    event = "KEYCODE_VOLUME_DOWN"
    set_input_keyevent(event)


def on_volume_close():
    event = "KEYCODE_VOLUME_MUTE"
    set_input_keyevent(event)


def on_main_menu():
    event = '3'
    set_input_keyevent(event)


def on_back_navigate():
    event = '4'
    set_input_keyevent(event)


def on_power():
    event = '26'
    set_input_keyevent(event)


def on_task_manage():
    event = "187"
    set_input_keyevent(event)


def on_landscape():
    event = ["content", "insert", "--uri", "content://settings/system", "--bind", "name:s:user_rotation", "--bind",
             "value:i:1"]
    shell(event)


def on_portrait():
    event = ["content", "insert", "--uri", "content://settings/system", "--bind", "name:s:user_rotation", "--bind",
             "value:i:0"]
    shell(event)


def on_key_press(event):
    command = ["adb", "shell", "input", 'keyevent', f'{desktop_to_android_keycode.get(event.keycode)}']
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def on_screencap():
    command = ['screencap', f'/sdcard/scrrenshot_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.png']
    shell(command)


def on_install_apk(root: Wm):
    root.geometry("800x600")
    label = tk.Label(root, width=400, height=600, bg="white", text="这是一个白色的Label", anchor="center")
    label.place(x=400, y=0)


def on_parent_move(sub_window, root, initial_geometry):
    # 防止父窗口移动
    root.geometry(initial_geometry)


def clear_child_window(root):
    initial_geometry = root.geometry()
    sub_window = tk.Toplevel(root)  # 创建子窗口
    sub_window.title("安装子窗口")  # 设置子窗口的标题
    sub_window.geometry("300x200")  # 设置子窗口的大小

    # 获取父窗口的位置和大小
    root.update_idletasks()  # 更新窗口信息
    parent_width = root.winfo_width()
    parent_height = root.winfo_height()
    parent_x = root.winfo_x()
    parent_y = root.winfo_y()

    # 计算子窗口的位置，使其居中显示
    sub_window_width = 300
    sub_window_height = 200
    sub_window_x = parent_x + (parent_width - sub_window_width) // 2
    sub_window_y = parent_y + (parent_height - sub_window_height) // 2

    sub_window.geometry(f"{sub_window_width}x{sub_window_height}+{sub_window_x}+{sub_window_y}")

    # 设置模态，禁用父窗口
    sub_window.grab_set()

    # 在子窗口中添加一个标签
    label = ttk.Label(sub_window, text="这是一个子窗口")
    label.pack(pady=20)

    # 在子窗口中添加一个关闭按钮
    close_button = ttk.Button(sub_window, text="关闭", command=sub_window.destroy)
    close_button.pack(pady=20)

    # 确保子窗口关闭时解除模态状态
    def on_closing():
        sub_window.grab_release()
        sub_window.destroy()

    sub_window.protocol("WM_DELETE_WINDOW", on_closing)
    # 捕获父窗口移动事件
    root.bind("<Configure>", lambda e: on_parent_move(sub_window, root, initial_geometry))
