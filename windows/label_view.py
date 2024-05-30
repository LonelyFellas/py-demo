import tkinter as tk
from windows.file_request import get_files_service


def label_view(root):
    root.geometry("800x600")  # 将主窗口的view的size设置成800x600
    create_left_border_view(root)
    label_root = create_label_view(root)

    res_list = get_files_service()
    print(res_list)
    apk_list = filter_apk_list(res_list)

    create_list_item(label_root)


def filter_apk_list(params_list):
    """ 过滤所有apk文件 """
    temp_list = []
    if params_list:
        for li in params_list:
            if li.get('name').endswith('.apk'):
                temp_list.append(li)

    return temp_list


def create_left_border_view(root):
    """ 创建左边框 """
    left_border = tk.Frame(root, width=2, height=600, bg="black")
    left_border.place(x=400, y=0)


def create_label_view(root):
    """ 创建Label """
    label = tk.Label(root, width=400, height=600, bg="#e9eef8", text="这是一个白色的Label", anchor="center")
    label.place(x=402, y=0)
    return label


def create_list_item(parent_root):
    canvas = tk.Canvas(parent_root, width=50, height=40)
    canvas.pack()
    canvas.create_rectangle(5, 5, 50, 30, outline="blue", width=2)
