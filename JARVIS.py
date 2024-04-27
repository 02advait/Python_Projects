import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

'''it speecks'''

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    ''' it takes microphone input from user and returns string as output'''   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print('Say that again please...')
        return "None"
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak("Good Evening!")
        print("Good Evening!")

speak("I am Jarvis Sir. Please tell me how may i help you")


if __name__ == "__main__":
    wishMe()
    while True :
        query = takeCommand().lower()
        # logic for executing task based on querry
        if 'wikipedia' in query:
            speak('Searching in Wikipedia...wait a while :)')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('Opening YouTube...wait a while :)')
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak('Opening google...wait a while :)')
            webbrowser.open("google.com")    
#        elif 'play music' in query:
#            music_dir = 'C:\Users\Advait\Music\Playlists'
#            songs = os.listdir
#            print(songs)
#            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sit, the time is {strTime}")
        elif 'vs code ' in query:
            vscodePath = ' C:\\Users\\Advait\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe '
            os.startfile(vscodePath)
        elif 'wallpaper' in query:
            wallpaperPath = ' "C:\\Users\\Advait\\AppData\\Local\\Programs\\Lively Wallpaper\\Lively.exe" '
            os.startfile(wallpaperPath)






