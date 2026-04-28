# 🔵 BLUE — Brain-Linked Utility Engine

> *"Blue online, Boss. Ready to assist."*

A smart, witty, and powerful personal AI voice assistant with a stunning 3D interface. Built to feel like a real AI companion — not just a chatbot.

---

## ✨ Features

### 🧠 AI Brain
- Powered by **Groq + LLaMA 3** for fast, intelligent responses
- Remembers conversations across sessions
- Always addresses you as **Boss**
- Natural, witty personality

### 🎙️ Voice
- Speaks back in male or female voice
- Random intro and exit lines — never repetitive
- Supports English, Hindi, and Hinglish

### 🌐 Web & App Control
- Open YouTube, Google, Instagram, Netflix, Spotify and more by command
- Google search by voice
- Open system apps like Notepad, Calculator, VS Code

### 💬 WhatsApp Automation
- Send WhatsApp messages by voice
- Built-in contacts system — no need to remember numbers
- Auto saves new contacts for future use

### 🌤️ Weather
- Real-time weather updates for any city
- Powered by OpenWeatherMap API

### 🔵 3D UI
- Stunning Three.js powered 3D orb
- Pulsing animation when Blue speaks
- Floating particles background
- Sleek dark space theme
- INITIALIZE screen on startup

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/vishesh-n-07/BLUE.git
cd BLUE
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup config files

Create `config.py`:
```python
GROQ_API_KEY = "your_groq_api_key_here"
```

Create `contacts.json`:
```json
{
    "mom": "+91XXXXXXXXXX",
    "dad": "+91XXXXXXXXXX"
}
```

### 4. Run BLUE

**Terminal mode:**
```bash
python blue.py
```

**3D UI mode:**
```bash
start ui.html
```

---

## 🖥️ Screenshots

### INITIALIZE Screen
![Initialize](screenshots/initialize.png)

### 3D Orb Interface
![Orb](screenshots/orb.png)

---

## ⚙️ Tech Stack

- **AI:** Groq API + LLaMA 3.3 70B
- **Voice Output:** pyttsx3
- **WhatsApp:** pywhatkit + pyautogui
- **Weather:** OpenWeatherMap API
- **3D UI:** Three.js
- **Automation:** Selenium + WebDriver

## 🔮 Roadmap

- [ ] Voice input (waiting for PyAudio Python 3.14 support)
- [ ] Gmail integration
- [ ] Spotify control
- [ ] Reminder system
- [ ] Mobile app version

---

## 💡 About

BLUE started as a personal project to build a Jarvis-like assistant that actually does real things — not just answers questions. Built with love by Vishesh. 🔵

[![GitHub](https://img.shields.io/badge/GitHub-vishesh--n--07-black?logo=github)](https://github.com/vishesh-n-07/BLUE)