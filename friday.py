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

def open_url(url):
    subprocess.run(["termux-open", url])

def open_app(activity):
    subprocess.run(["am", "start", "-n", activity])

WEBSITES = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "github": "https://github.com",
    "stackoverflow": "https://stackoverflow.com",
}

memory = load_memory()

subprocess.run([
   "termux-notification",
   "--content", "Welcome To friday"
])

speak("Welcome To friday")

while True:
    user_input = input("You: ").strip()
    command = user_input.lower()

    if command == "what time is it?":
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}.")

    elif command.startswith("remember "):
        memory_text = user_input[9:].strip()

        if " is " in memory_text:
            key, value = memory_text.split(" is ", 1)
            key = key.strip().lower()

            if key.startswith("my "):
              key = key[3:]
            value = value.strip()
            memory[key] = value
            save_memory(memory)
            speak("I'll remember that.")
        else:
            speak("Tell me what you want me to remember.")

    elif command == "what do you remember":
     if not memory:
         speak(" I don't remember anything yet.")
     else:
         speak(" Here's what I remember:")
         for key, value in memory.items():
            print(f"- {key}: {value}")

    elif command.startswith("what is my "):
      key = command[11:].strip()

      if key in memory:
          speak(f"Your {key} is {memory[key]}.")
      else:
          speak(f"I don't remember your {key} yet.")

    elif command.startswith("open "):
       site = command.replace("open ", "").strip()

       if site in WEBSITES:
          print(f"FRIDAY: Opening {site.title()}...")
          open_url(WEBSITES[site])
       else:
          print(f"FRIDAY: Sorry, I don't know how to open '{site}' yet.")

    elif command == "check my battery":
        # Decode bytes output to string for secure json parsing
        battery_data = subprocess.check_output(["termux-battery-status"]).decode('utf-8')
        battery = json.loads(battery_data)
        percentage = battery["percentage"]
        speak(f"Your battery is {percentage} percent.")

    elif command == "hello friday":
        name = memory.get("name", "friend")
        speak(f"Hello {name}. how can i assist you today!")

    elif command == "where am i?":
        # Decode bytes output to string for secure json parsing
        location_data = subprocess.check_output(["termux-location", "-p", "network"]).decode('utf-8')
        location = json.loads(location_data)

        latitude = location["latitude"]
        longitude = location["longitude"]
        speak(f"your latitude is {latitude} and your longitude is {longitude}. or just search it on maps")

    elif command == "torch on":
        speak("Turning on the flashlight.")
        subprocess.run(["termux-torch", "on"])

    elif command == "torch off":
        speak("Turning off the flashlight.")
        subprocess.run(["termux-torch", "off"])

    elif command.startswith("forget "):
      key = command.replace("forget my ", "").strip()

      if key in memory:
         del memory[key]
         save_memory(memory)
         speak(f"Okay, I forgot your {key}.")
      else:
         speak(f"I don't remember your {key}.")

    elif command == "tell me a joke":
        subprocess.run([
            "termux-toast",
            "Hey Aymen! we are gonna blow the ai world man 💣💣"
        ])

    elif command == "exit":
      name = memory.get("name", "friend")
      speak(f"Goodbye {name}. See you next 😁")
      break

    else:
        speak("sorry but i didn't learn this yet. ok! 😁.")

