import psutil


def get_battery_info():

    battery = psutil.sensors_battery()
    if battery is not None:
        percent = battery.percent
        power_plugged = battery.power_plugged

        return power_plugged, percent
