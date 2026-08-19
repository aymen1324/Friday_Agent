import json 
import subprocess

def open_url(url):
    subprocess.run(["termux-open", url])

def open_app(activity):
    subprocess.run(["am", "start", "-n", activity])

def load_websites():
    with open("data/websites.json", "r") as file:
        return json.load(file)

def save_websites(websites):
    with open("data/websites.json", "w") as file:
        json.dump(websites, file, indent=4)
        
def load_apps():
    with open("data/apps.json", "r") as file:
        return json.load(file)
        