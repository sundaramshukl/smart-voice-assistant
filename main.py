import speech_recognition as sr
import pyttsx3
from nlp_utils import interpret_command
from weather import get_weather
from music_player import play_music
import wikipedia
import webbrowser

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Could not connect to the service.")
            return ""

def main():
    speak("Hello! I am your smart assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            task = interpret_command(command)

            if task['intent'] == 'weather':
                city = task.get('city', 'Delhi')
                report = get_weather(city)
                speak(report)

            elif task['intent'] == 'music':
                play_music()
                speak("Playing your music now.")

            elif task['intent'] == 'query':
                try:
                    result = wikipedia.summary(task['query'], sentences=2)
                    speak(result)
                except:
                    speak("Sorry, I couldn't find information on that.")

            elif task['intent'] == 'exit':
                speak("Goodbye!")
                break

            else:
                speak("I'm not sure how to help with that yet.")

if __name__ == "__main__":
    main()
