import psutil
import schedule
import time

def print_cpu_temp():

    data = psutil.sensors_temperatures().get('coretemp')[0].current
    print(data)
    # temp = psutil.sensors_temperatures().get('coretemp')[0].current
    # print(f"CPU temperature: {temp}°C")

schedule.every(10).seconds.do(print_cpu_temp)

while True:
    schedule.run_pending()
    time.sleep(1)