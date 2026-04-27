# blue.py
# BLUE's voice and AI brain

import pyttsx3
import speech_recognition as sr
from groq import Groq
from config import load_config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import urllib.parse
import json
import os

MEMORY_FILE = "memory.json"

def save_memory(conversation_history):
    """Save conversation history to file"""
    # Keep only last 20 messages to avoid huge files
    recent = conversation_history[-20:]
    with open(MEMORY_FILE, "w") as f:
        json.dump(recent, f, indent=2)

def load_memory():
    """Load previous conversation history"""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []
# Load config
config = load_config()
NAME = config["name"]
VOICE = config["voice"]
LANGUAGE = config["language"]

# Your Groq API key
GROQ_API_KEY = "your_groq_api_key_here"

# Initialize Groq
client = Groq(api_key=GROQ_API_KEY)



def speak(text):
    """Blue speaks"""
    print(f"\n🔵 Blue: {text}\n")
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    if VOICE == "female":
        engine.setProperty("voice", voices[1].id)
    else:
        engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 175)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen():
    """Temporary text input until PyAudio supports Python 3.14"""
    # TODO: Replace with voice input when PyAudio supports Python 3.14
    # recognizer = sr.Recognizer()
    # with sr.Microphone() as source:
    #     audio = recognizer.listen(source)
    #     return recognizer.recognize_google(audio)
    
    try:
        user_input = input(f"👤 {NAME} (Boss): ")
        return user_input.lower()
    except KeyboardInterrupt:
        return "exit"

def think(user_input, conversation_history):
    """Blue thinks using Groq AI"""
    
    system_prompt = f"""You are Blue, a smart and witty personal voice assistant.
Your user's name is {NAME} and you always call them 'Boss'.
You speak in {LANGUAGE}.
Keep responses short and conversational — this is a voice assistant, not a text chat.
Be helpful, confident, and occasionally witty.
Always address the user as Boss.
You have memory of previous conversations with Boss. 
If asked what you remember, summarize the previous conversation history provided."""

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt}
        ] + conversation_history,
        max_tokens=150
    )

    reply = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    return reply, conversation_history
import webbrowser
import os
import subprocess

def handle_command(user_input):
    """Handle system commands"""

    # WhatsApp send - check FIRST before anything else
    if "whatsapp" in user_input and "send" in user_input:
        speak("Who should I message, Boss?")
        contact = input("👤 Contact name: ")
        speak("What's the message, Boss?")
        message = input("👤 Message: ")
        return send_whatsapp(contact, message)

    # Open websites
    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "gmail": "https://www.gmail.com",
        "github": "https://www.github.com",
        "whatsapp": "https://web.whatsapp.com",
        "instagram": "https://www.instagram.com",
        "twitter": "https://www.twitter.com",
        "linkedin": "https://www.linkedin.com",
        "netflix": "https://www.netflix.com",
        "spotify": "https://www.spotify.com",
    }

    # Open apps
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "chrome": "chrome.exe",
        "vs code": "code",
    }

    # Check for website commands
    for site, url in websites.items():
        if site in user_input:
            webbrowser.open(url)
            return f"Opening {site} for you, Boss!"

    # Check for app commands
    for app, command in apps.items():
        if app in user_input:
            subprocess.Popen(command)
            return f"Opening {app}, Boss!"

    # Handle search
    if "search" in user_input or "look up" in user_input:
        query = user_input.replace("search", "").replace("look up", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching for {query}, Boss!"

    # Weather commands
    if "weather" in user_input:
        words = user_input.lower()
        words = words.replace("what's the weather in", "")
        words = words.replace("whats the weather in", "")
        words = words.replace("weather in", "")
        words = words.replace("weather", "")
        words = words.strip()
        city = words if words else "Bangalore"
        return get_weather(city)

    return None
import requests

def get_weather(city):
    """Get real weather data"""
    API_KEY = "3b1254efb34d3d13229ed495d6197847"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        print(f"API Response: {data}")
        
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            city_name = data["name"]
            
            return f"Boss, in {city_name} it's {temp}°C, feels like {feels_like}°C. Conditions are {condition} with {humidity}% humidity."
        else:
            return f"Couldn't find weather for {city}, Boss."
    except:
        return "Sorry Boss, I couldn't fetch the weather right now."

def send_whatsapp(contact_name, message):
    """Send WhatsApp message via pywhatkit"""
    try:
        import pywhatkit
        import pyautogui
        import json

        # Load contacts
        with open("contacts.json", "r") as f:
            contacts = json.load(f)

        # Find contact
        contact_key = contact_name.lower().strip()
        phone = None
        for name, number in contacts.items():
            if name in contact_key or contact_key in name:
                phone = number
                break

        if not phone:
            speak(f"I don't have {contact_name} in your contacts Boss. What's their number?")
            phone = input("👤 Phone number (with country code): ")
            # Save for next time
            contacts[contact_name.lower()] = phone
            with open("contacts.json", "w") as f:
                json.dump(contacts, f, indent=2)
            speak(f"Got it Boss. I've saved {contact_name} for next time.")

        speak(f"Sending message to {contact_name}, Boss. WhatsApp will open in a moment.")
        
        pywhatkit.sendwhatmsg_instantly(phone, message, wait_time=20, tab_close=False)
        
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(2)
        
        return f"Message sent to {contact_name}, Boss!"
    
    except Exception as e:
        return f"Sorry Boss, couldn't send. Error: {str(e)}"
    
if __name__ == "__main__":
    import random
    
    conversation_history = load_memory()
    
    if conversation_history:
        welcomeback_lines = [
            f"Hey Boss! Good to see you again. What are we doing today?",
            f"Welcome back Boss! I've been waiting. What do you need?",
            f"Boss is back! Let's get to work. What's on your mind?",
            f"Ah, Boss returns! Ready when you are.",
            f"Good to have you back Boss. What can I do for you?",
            f"Boss! I remember where we left off. What's next?",
        ]
        speak(random.choice(welcomeback_lines))
    else:
        first_time_lines = [
            f"Hello Boss! I'm Blue, your personal assistant. How can I help you today?",
            f"Blue online, Boss. Ready to assist. What do you need?",
            f"Hey Boss! Blue here. What are we working on today?",
            f"Good to meet you Boss! I'm Blue. Ask me anything.",
            f"Blue activated, Boss. All systems ready. How can I help?",
        ]
        speak(random.choice(first_time_lines))
    
    while True:
        user_input = listen()
        
        if not user_input:
            continue
        
        if any(word in user_input for word in ["exit", "bye", "quit", "goodbye"]):
            save_memory(conversation_history)
            exit_lines = [
                "Goodbye Boss! I'll remember everything. See you soon!",
                "Later Boss! It was a pleasure. Blue signing off.",
                "Alright Boss, take care! I'll be here when you need me.",
                "Blue going offline Boss. Have a great one!",
                "See you soon Boss! Don't forget, I remember everything. 😄",
                "Signing off Boss. Stay awesome!",
            ]
            speak(random.choice(exit_lines))
            break   
        
        command_response = handle_command(user_input)
        if command_response:
            speak(command_response)
        else:
            response, conversation_history = think(user_input, conversation_history)
            speak(response)
            save_memory(conversation_history)