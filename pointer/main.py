import ctypes
import threading


class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]


def get_mouse_position():
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y


def display():
    x, y = get_mouse_position()
    print(f"当前鼠标的位置：x={x}, y={y}")
    threading.Timer(1, display).start()


if __name__ == '__main__':
    display()