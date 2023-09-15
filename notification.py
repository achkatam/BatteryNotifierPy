from plyer import notification


def notify():
    notification_title = "Battery notification"
    notification_message = "Battery is at 80% at this moment."
    notification_timeout = 5  # seconds

    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=notification_timeout
    )
