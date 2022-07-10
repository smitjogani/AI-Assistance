import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import datetime
import pyaudio

# use inbuilt voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# set voice
engine.setProperty('voice', voices[1].id)

# this  function give responce


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wishMe function wish with looking the time


def wishMe():
    # take hour in int form
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning...")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon...")

    elif hour >= 18 and hour < 22:
        speak("Good Evening...")

    else:
        speak("Good Night...")

    speak("I'm benz sir. Plese tell me how may i help you?")


# it take the microphone input from the user and return string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing....")
        r.pause_threshold = 1
        audio = sr.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User says : {query} \n")

    except Exception as e:
        # print(e)
        print("Say that again plese....")
        return "None"
    return query

# for sending email
def send_Email(to , content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()    
    server.starttls()
    server.login('psmit1935@gmail.com' , 'SmIt(+1909')
    server.sendmail(psmitjogani1935@gmail.com, to, content)
    server.close()
if __name__ == '__main__':
    wishMe()

    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searcing Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        
        elif 'play music' in query:
            music_dir = ''
            songs  = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        
        elif 'the time' in query:
            strTime = datetime.datetime().now().strftime("%H:%M:%S")
            speak(f"The time is {strTime} ")
            
        elif 'open android studio' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio"
            os.startfile(codePath)
        
        elif 'emaail to herry' in query:
            try:
                speak("What should you say?")
                contant = takeCommand()
                to = "psmit1935@gmail.com"
                sendEmail(to, content)
                speak("Email has been send!!")
            except Exception as e:
                print(e)
                speak("Sorry sir!!! I can't able to send email")
                
        elif 'quite' in query:
            exit()