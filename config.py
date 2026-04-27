# config.py
# Stores BLUE's settings and user preferences

import json
import os

CONFIG_FILE = "user_config.json"

def setup_blue():
    """First time setup for BLUE"""
    print("\n" + "="*40)
    print("🔵 Welcome to BLUE Setup")
    print("Brain-Linked Utility Engine")
    print("="*40 + "\n")

    name = input("What's your name, Boss? → ")
    
    print("\nChoose your voice:")
    print("1. Male")
    print("2. Female")
    voice_choice = input("Enter 1 or 2 → ")
    voice = "male" if voice_choice == "1" else "female"

    print("\nChoose your language:")
    print("1. English")
    print("2. Hindi")
    print("3. Hinglish")
    lang_choice = input("Enter 1, 2 or 3 → ")
    lang_map = {"1": "english", "2": "hindi", "3": "hinglish"}
    language = lang_map.get(lang_choice, "english")

    config = {
        "name": name,
        "voice": voice,
        "language": language,
        "assistant_name": "Blue"
    }

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

    print(f"\n✅ Setup complete! Hello {name}, I'm Blue. Let's get started!\n")
    return config

def load_config():
    """Load existing config or run setup"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    else:
        return setup_blue()

if __name__ == "__main__":
    config = load_config()
    print(config)