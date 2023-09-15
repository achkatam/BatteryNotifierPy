import time
from notification import notify
from get_battery_info import get_battery_info
import sys
import create_icon

if __name__ == "__main__":

    battery_info = get_battery_info()
    power_plugged = battery_info[0]
    battery_percent = battery_info[1]

    while True:
        if power_plugged is False and battery_percent == 51:
            notify()
            time.sleep(5)
            sys.exit()
        else:
            time.sleep(5)
        battery_info = get_battery_info()
        power_plugged = battery_info[0]
        battery_percent = battery_info[1]
