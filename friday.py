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

    elif command == "battery":
        battery = subprocess.check_output(["termux-battery-status"])
        battery = json.loads(battery)

        percentage = battery["percentage"]
        speak(f"Your battery is {percentage} percent.")
                                  
    elif command == "hello friday":
       speak("Hello Aymen! how can i assist you today")


    elif command == "torch on":
        speak("Turning on the flashlight.")
        subprocess.run(["termux-torch", "on"])

    elif command == "torch off":
       speak("Turning off the flashlight.")
       subprocess.run(["termux-torch", "off"])

    elif command == "toast":
       subprocess.run([
        "termux-toast",
        "Hello Aymen! FRIDAY is alive!"
       ])

    elif command == "exit":
        speak("Goodbye Aymen.")
        break

    else:
        speak("I don't understand that command yet.")
