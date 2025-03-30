import psutil

cpu_usage=psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}$")


cpu_usage=85

if cpu_usage >80:
    print("High CPU Usage! Scale Up")
else:
    print("CPU is Noraml")