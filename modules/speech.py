import subprocess

def speak(message):
    print(f"FRIDAY: {message}")
    subprocess.run(["termux-tts-speak", message])
