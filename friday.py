import json
import subprocess
from datetime import datetime

from modules.memory import load_memory, save_memory

from modules.speech import speak

from modules.launcher import (
    open_url,
    open_app,
    load_websites,
    save_websites,
    load_apps,
)

from modules.device import get_location

from modules.device import get_battery

from modules.device import torch_on, torch_off, show_toast, get_current_time

from modules.device import get_location

memory = load_memory()

websites = load_websites()

apps = load_apps()

subprocess.run([
   "termux-notification",
   "--content", "Welcome To friday"
])

speak("Welcome To friday")

while True:
    user_input = input("You: ").strip()
    command = user_input.lower()

    if command == "hello friday":
        name = memory.get("name", "friend")
        speak(f"Hello {name}. how can i assist you today!")
    
    elif command == "what time is it?":
        now = get_current_time()
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
          
    elif command.startswith("forget "):
      key = command.replace("forget my ", "").strip()

      if key in memory:
         del memory[key]
         save_memory(memory)
         speak(f"Okay, I forgot your {key}.")
      else:
         speak(f"I don't remember your {key}.")

    elif command.startswith("open ") and command.endswith(" website"):
       site = command.replace("open ", "").replace(" website", "").strip()

       found = False

       for website in websites:
        if website["id"] == site:
          print(f"FRIDAY: Opening {website['name']}...")
          open_url(website["url"])
          found = True
          break

       if not found:
           print(f"FRIDAY: Sorry, I don't know how to open '{site}' yet.")

    elif command.startswith("add website "):
     parts = command.split()

     if len(parts) < 4:
        print("FRIDAY: Usage: add website <id> <url>")
     else:
        # Added [2] and [3] here to grab the specific parts
        website_id = parts[2]
        url = parts[3]
        
        exists = False

        for website in websites:
          if website["id"] == website_id:
           exists = True
           break

        new_website = {
            "id": website_id,
           "name": website_id.title(),
           "url": url,
           "category": "Custom"
       }

        if exists:
         print(f"FRIDAY: I already know {website_id.title()}.")
        else:
         websites.append(new_website)
         save_websites(websites)
         
         print(f"FRIDAY: Added {website_id.title()}!")
         
    elif command.startswith("open"): 
       app = command.replace("open ", "").strip()

       found = False

       for application in apps:
         if application["id"] == app:
           print(f"FRIDAY: Launching {application['name']}...")
           open_app(application["package"])
           found = True
           break

       if not found:
            print(f"FRIDAY: Sorry, I don't know how to open '{app}' yet.")
           
    elif command == "check my battery":
       percentage = get_battery()
       speak(f"Your battery is {percentage} percent.")


    elif command == "where am i?":
        speak("Locating you now...")
        lat, lng = get_location()

        if lat and lng:
            speak(f"Your latitude is {lat} and your longitude is {lng}.")
        else:
            speak("I couldn't retrieve your location. Please make sure GPS and location permissions are turned on.")

    elif command == "torch on":
        torch_on(speak)

    elif command == "torch off":
        torch_off(speak)

    elif command == "tell me a joke":
        show_toast("Hey Aymen! we are gonna blow the ai world man 💣💣")

    elif command == "exit":
      name = memory.get("name", "friend")
      speak(f"Goodbye {name}. See you next 😁")
      break

    else:
        speak("sorry but i didn't learn this yet. ok! 😁.")

