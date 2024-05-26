import psutil
import os

current_pid = psutil.Process(os.getpid())
print(f"Process ID: {current_pid.pid}")
print(f"Process Name: {current_pid.name()}")
print(f"Process Status: {current_pid.status()}")
