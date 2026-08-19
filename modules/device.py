import json 
import subprocess
from datetime import datetime

def get_battery():
    battery_data = subprocess.check_output(
        ["termux-battery-status"]
    ).decode("utf-8")
    battery = json.loads(battery_data)
    return battery["percentage"]

def get_location():
    try:
        location_data = subprocess.check_output(
            ["termux-location", "-p", "network"],
            timeout=10
        ).decode('utf-8')

        location = json.loads(location_data)
        return location.get("latitude"), location.get("longitude")

    except Exception:
        return None, None
  
def torch_on(speak_func=None):
    if speak_func:
        speak_func("Turning on the flashlight.")
    subprocess.run(["termux-torch", "on"])

def torch_off(speak_func=None):
    if speak_func:
        speak_func("Turning off the flashlight.")
    subprocess.run(["termux-torch", "off"])

def show_toast(message):
    subprocess.run(["termux-toast", message])

def get_current_time():
    return datetime.now().strftime("%I:%M %p")