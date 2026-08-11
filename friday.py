import json
import subprocess
from datetime import datetime


def speak(message):
    print(f"FRIDAY: {message}")
    subprocess.run(["termux-tts-speak", message])


while True:
    command = input("You: ").lower().strip()

    if command == "time":
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}.")

    elif command == "hello":
        speak("hello Aymen!! Aymen! what do you wanna chek")

    elif command == "battery":
        battery = subprocess.check_output(["termux-battery-status"])
        battery = json.loads(battery)

        percentage = battery["percentage"]
        speak(f"Your battery is {percentage} percent.")

    elif command == "exit":
        speak("Goodbye Aymen.")
        break

    else:
        speak("I don't understand that command yet.")
