import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
#import smtplib
#import openai


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)






'''it speecks'''
'''takes audio input from microphone'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



''' it takes microphone input from user and returns string as output'''
'''it can give errors so we use try, except and return'''
def takeCommand():       
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




'''gives the current date and time, and wishes me.:D '''
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



def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")





speak("Hello I an  Jarvis A.I..  how may i help you Sir")

if __name__ == "__main__":
    wishMe()
    while True :
        query = takeCommand().lower()
        # logic for executing task based on querry
        if 'xyz' in query:
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
        elif 'vs code' in query:
            vscodePath = "C:\\Users\\Advait\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodePath)
#        elif 'wallpaper' in query:
#            wallpaperPath = "C:\\Users\\Advait\\AppData\\Local\\Programs\\Lively Wallpaper\\Lively.exe"
#            os.startfile(wallpaperPath)
        elif "google" in query:
            searchGoogle(query)
