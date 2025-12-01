# JARVIS-Voice-Assistant-System

JARVIS is a Python-based voice assistant that listens to your voice, understands your commands, and performs real-time tasks such as opening applications, searching online, sending WhatsApp messages, checking weather, and generating AI-powered responses.

This project uses speech recognition, text-to-speech (TTS), automation tools, and Gemini AI to create a hands-free assistant experience similar to Iron Man's JARVIS.

## 🎥 Demo Video

Click below to watch the live demo of the JARVIS Voice Assistant:

🔗 **Demo Link:**  
https://drive.google.com/drive/folders/13jh94CazwuqdFByrb291WlImbVJlmilF?usp=sharing

## 🛠 Features

- Greet the user according to the time of day (morning, afternoon, evening)

- Recognize voice commands using Google Speech Recognition

- Speak responses using pyttsx3 (offline TTS)

- Google & YouTube search via voice

- Wikipedia search with spoken summary

- Open system applications: Chrome, Notepad

- Open LinkedIn profile directly

- Real-time weather report using OpenWeather API

- Send WhatsApp messages instantly to saved contacts

- AI “Think Mode” using Google Gemini (explain, write, generate answers)

- Tell jokes and respond to small talk

- Exit gracefully with a voice command

## 💻 Requirements

- Python 3.11 or higher
- Working microphone & stable internet connection
- Gemini API key & OpenWeather API key

## 💻 Requirements

- Python 3.11 or higher

## How to run?

1. Create a virtual environment:

   ```bash
   conda create -n jarvis python=3.11 -y
   ```

2. Activate virtual environment:

   ```bash
   conda activate jarvis
   ```

3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the JARVIS script:

   ```bash
   python jarvis.py
   ```

👨‍💻 Author
Abdullah Al Maruf

📜 License
This project is open-source and free to use for learning and personal use.
