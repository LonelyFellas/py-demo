import os

DEMO = 'demo-dir'
NEW_NAME = 'new2-name'

os.chdir("modify-file-name")
current_dir = os.getcwd()

subdir = os.listdir(current_dir)

if DEMO in subdir and os.path.isdir(os.path.join(current_dir, DEMO)):
    os.chdir(DEMO)
    demo_dir = os.getpid()

    sub_demo_dir = os.listdir()
    for i, sub_file in enumerate(sub_demo_dir):
        new_name = f"{NEW_NAME}{i}.txt"
        os.rename(sub_file, new_name)
