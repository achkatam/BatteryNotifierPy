import time
from notification import notify
from get_battery_info import get_battery_info
import create_icon

if __name__ == "__main__":

    battery_info = get_battery_info()
    power_plugged = battery_info[0]
    battery_percent = battery_info[1]

    while battery_percent < 80:
        if power_plugged is True and battery_percent >= 77:
            notify()
            create_icon.create_system_icon()
            time.sleep(60)
            battery_info = get_battery_info()
