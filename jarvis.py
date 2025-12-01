import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess
import pywhatkit
import requests

import google.generativeai as genai
genai.configure(api_key="AIzaSyAGaW6zT1ScNE-7bsDCgDOJYWfoAfKN-ck")
model = genai.GenerativeModel("gemini-2.5-flash")

#whatsapp-contact
contacts = {
    "abir": "+8801611153510",
    "nahid": "+8801600246257",
    "Nahid": "+8801600246257",
    "shagor": "+8801717505550"
}


#weather-api

WEATHER_API_KEY = "e98441517a8e43a2ad84cb0ed735045e"

#function to get weather report
def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        data = requests.get(url).json()

        if data["cod"] != 200:
            return None

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        report = f"The weather in {city} is {condition} with a temperature of {temp} degrees Celsius and humidity of {humidity} percent."
        return report

    except:
        return None



# Logging configuration
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"
os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# Activating voice from our system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 170)
engine.setProperty('voice', voices[0].id)


def speak(text):
    """This function takes a string input and converts it to speech.
    
    Args:
        text 
    Returns:
        voice output of the input text
    """
    for chunk in text.split('. '):
        engine.say(chunk)
        engine.runAndWait()


def takeCommand():
    """
    This funnction is for listening user audio and convert to text
    Returns:
        text converted from user audio
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        logging.info(e)
        print("Say that again please...")
        return "None"
    
    return query


def greet():
    """
    This function greets the user according to the time
    
    Returns:
        voice output of greeting message
    """
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("Welcome to the Jarvis Voice Assistant System")


greet()


#whatsapp-contact-matching
def find_contact(spoken, contacts):
    spoken = spoken.lower().strip()
    for key in contacts.keys():
        if key in spoken:   
            return contacts[key]
    return None



while True:
    query = takeCommand().lower()

    #name
    if "name" in query:
        logging.info("User asked for name")
        speak("My name is Jarvis, your personal voice assistant.")

    #time
    elif "time" in query:
        logging.info("User asked for time")
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    #bye-function
    elif "bye" in query:
        logging.info("User ended the session")
        speak("Goodbye Sir! Have a nice day.")
        break

    #joke
    elif "a joke" in query:
        logging.info("User asked for a joke")
        joke = random.choice([
            "Why did the computer go to the doctor? Because it had a virus!",
            "I would tell you a UDP joke, but you might not get it.",
            "Debugging is like being a detective in a crime movie where you are also the murderer."
        ])
        speak(joke)

    #conversation
    elif "single" in query:
        logging.info("Relationship status asked")
        speak("Yes sir, no one wants to date a voice assistant.")

    #conversation
    elif "funny" in query:
        logging.info("User said Jarvis is funny")
        speak("I try my best to make you smile, sir.")

    #linkedin   
    elif "linkedin" in query or "open linkedin" in query:
        logging.info("LinkedIn profile opened")
        speak("Opening your LinkedIn profile")
        webbrowser.open("https://www.linkedin.com/in/abdullah-al-maruf-0a2615373/")

    #chrome
    elif "open chrome" in query:
        logging.info("Opening Chrome")
        speak("Opening Google Chrome")
        path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        subprocess.Popen([path])

    #notepad
    elif "open notepad" in query:
        logging.info("Opening Notepad")
        speak("Opening Notepad")
        subprocess.Popen(["notepad.exe"])

    #youtube-search
    elif "youtube search" in query:
        logging.info("YouTube search triggered")
        yt_query = query.replace("youtube search", "")
        speak(f"Searching YouTube for {yt_query}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={yt_query}")

    #google-search
    elif "google search" in query:
        logging.info("Google search triggered")
        search_query = query.replace("google search", "")
        speak(f"Searching Google for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

    #wikipedia
    elif "wikipedia" in query:
        logging.info("Wikipedia command triggered")
        speak("Searching Wikipedia...")
        wiki_query = query.replace("wikipedia", "")

        try:
            results = wikipedia.summary(wiki_query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            logging.info("Wikipedia summary provided")
        except:
            speak("I am sorry, I couldn't find any information on that topic.")
            logging.error("Wikipedia search failed")


    #ai-think-gemini
    elif "think" in query or "explain" in query or "write" in query or "generate" in query:
        logging.info("AI think command triggered")
        try:
            speak("Thinking... please wait.")
            response = model.generate_content(
                f"Give a short clear reply within 4 to 5 sentences: {query}"
            )
            answer = response.text.strip()
            print(answer)

            for chunk in answer.split('. '):
                speak(chunk)

            logging.info("AI answer provided")
        except Exception as e:
            speak("Sorry sir, I could not think about that.")
            logging.error(f"AI error: {e}")


    #whatapp-message

    elif "whatsapp" in query:
        speak("Whom do you want to message?")
        name = takeCommand().lower().strip()

        number = find_contact(name, contacts)

        if number:
            speak("What is the message?")
            message = takeCommand()

            speak(f"Sending WhatsApp message to {name}.")

            try:
                pywhatkit.sendwhatmsg_instantly(number, message)
                speak("Message sent successfully.")
                logging.info(f"WhatsApp message sent instantly to {name}")

            except Exception as e:
                speak("Sorry sir, I could not send the message.")
                logging.error(f"WhatsApp error: {e}")
        else:
            speak("Sorry, I don't have this contact saved.")


    elif "weather" in query:
        logging.info("Weather command triggered")
        speak("Which city's weather do you want to know?")

        # Keep asking until a city is captured
        city = None
        while city is None or city.strip() == "" or city == "none":
            city = takeCommand().lower().strip()
            
            if city is None or city.strip() == "" or city == "none":
                speak("I didn't catch the city name. Please say it again.")

        speak("Checking the weather. Please wait.")
        report = get_weather(city)

        if report:
            speak(report)
            logging.info(f"Weather report given for {city}")
        else:
            speak("Sorry sir, I could not get the weather information.")
            logging.error("Weather API failed")

    else:
        logging.warning("Unrecognized command")
        speak("I am sorry, I didn't understand that command.")
