import subprocess

def listen():
    """
    Listen for a voice command and return it as text using Termux Speech-to-Text.
    """
    try:
        result = subprocess.run(
            ["termux-speech-to-text"],
            capture_output=True,
            text=True
        )

        return result.stdout.strip().lower()

    except Exception:
        return ""
