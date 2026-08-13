import json
import subprocess
from datetime import datetime

def load_memory():
    try:
        with open("memory.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_memory(memory):
    with open("memory.json", "w") as file:
        json.dump(memory, file, indent=4)

def speak(message):
    print(f"FRIDAY: {message}")
    subprocess.run(["termux-tts-speak", message])

memory = load_memory()

while True:
    command = input("You: ").lower().strip()

    if command == "what time is it?":
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}.")

    elif command == "what is my name?":
         memory = load_memory()
         speak(f"Your name is {memory['name']}.")

    elif command == "check my battery":
        battery = subprocess.check_output(["termux-battery-status"])
        battery = json.loads(battery)

        percentage = battery["percentage"]
        speak(f"Your battery is {percentage} percent.")

    elif command == "hello friday":
       speak("Hello Aymen! how can i assist you today")

    elif command == "where am i?":
       location = subprocess.check_output(["termux-location",
                                            "-p",
                                            "network"])
       location = json.loads(location)

       latitude = location["latitude"]
       longitude = location["longitude"]
       speak(f"your latitude is {latitude} and your longitude is {longitude}.or just search it on maps")

    elif command == "torch on":
        speak("Turning on the flashlight.")
        subprocess.run(["termux-torch", "on"])

    elif command == "torch off":
       speak("Turning off the flashlight.")
       subprocess.run(["termux-torch", "off"])

    elif command == "tell me a joke":
       subprocess.run([
        "termux-toast",
        "Hey Aymen! we are gonna blow the ai world man 💣💣"
       ])

    elif command == "exit":
        speak("Goodbye Aymen. see you next 😁")
        break

    else:
        speak("sorry but i didn't learn this yet ok. iam still young for that 😁.")
