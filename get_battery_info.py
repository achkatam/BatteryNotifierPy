import psutil


def get_battery_info():

    status = ""
    battery = psutil.sensors_battery()
    if battery is not None:
        percent = battery.percent
        power_plugged = battery.power_plugged

        if power_plugged:
            status = "charging"
        else:
            status = "not charging"
        return power_plugged, percent
    else:
        return "No battery information is available at this moment."
