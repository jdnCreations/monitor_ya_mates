from datetime import datetime
import psutil
import requests
import platform
import time
import GPUtil

# get cpu, ram, gpu, etc info from pc
boot_time = psutil.boot_time()
current_time = time.time()
cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent
gpus = GPUtil.getGPUs()
gpu_temps = gpus[0].temperature

# send a post request with that data to the server
data = {"boot_time": boot_time, "current_time": current_time,
        "cpu_usage": cpu_usage, "ram_usage": ram_usage, "gpu_temp": gpu_temps}

res = requests.post("http://127.0.0.1:5000/log", json=data)
print(res.json())
