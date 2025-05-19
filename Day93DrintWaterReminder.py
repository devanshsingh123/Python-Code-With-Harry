import time
from plyer import notification

# Reminder message
WATER_REMINDER = "Hey Dev! Time to drink your water 💧"

# Time interval in seconds (1 hour = 3600 seconds)
REMINDER_INTERVAL = 3600  # Change to 7200 for 2 hours

try:
    while True:
        # Send desktop notification
        notification.notify(
            title="Hydration Reminder",
            message=WATER_REMINDER,
            timeout=10,  # seconds the notification stays on screen
            app_name="Water Reminder"
            # app_icon="path/to/icon.ico"  # Optional: add path to an icon
        )

        # Wait for the next reminder
        time.sleep(REMINDER_INTERVAL)

except KeyboardInterrupt:
    print("\nWater reminder stopped by user.")
