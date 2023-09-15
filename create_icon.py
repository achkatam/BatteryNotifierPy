import time
import pystray
from get_battery_info import get_battery_info


def create_system_icon():
    icon = pystray.Icon("BatteryNotifier")
    icon.icon = pystray.Icon("BatteryNotifier")
    icon.title = "BatteryNotifier"
    icon.menu = pystray.Menu(
        pystray.MenuItem(
            "Exit",
            lambda: icon.stop()
        )
    )
    return icon


def update_tray_icon(icon):
    while True:
        battery_info = get_battery_info()
        icon.update_menu()
        icon.update_menu_item(0, label=battery_info)
        time.sleep(60)
        return icon
