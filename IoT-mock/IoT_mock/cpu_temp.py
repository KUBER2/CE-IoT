import psutil
import schedule
import time

def print_cpu_temp():
    temp = psutil.sensors_temperatures().get('coretemp')[0].current
    print(temp)

schedule.every(1).minutes.do(print_cpu_temp)

while True:
    schedule.run_pending()
    time.sleep(1)