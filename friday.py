import json
import subprocess
from datetime import datetime

# Current time
now = datetime.now().strftime("%I:%M %p")

# Get battery information
battery = subprocess.check_output(["termux-battery-status"])
battery = json.loads(battery)

percentage = battery["percentage"]

message = (
    f"Hello Aymen! "
    f"The time is {now}. "
    f"Your battery is {percentage} percent."
)

print(message)

# Speak
subprocess.run(["termux-tts-speak", message])

# Notification
subprocess.run([
    "termux-notification",
    "--title", "FRIDAY",
    "--content", message
])
