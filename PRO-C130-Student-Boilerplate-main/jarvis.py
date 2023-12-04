import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
from gtts import gTTS
import playsound
from io import BytesIO
from PIL import Image
import openai

openai.api_key = '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'  

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sarcasm():
    global num
    num += 1
    query = takeCommand().lower()
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou:{str(query)}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    stop = ["\n", " Human:", ]
    answer = response.choices[0].text.strip()
    speak(answer)

def grammar_correction():
    global num
    num += 1
    query = takeCommand().lower()
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Correct this to standard English:\n\n{str(query)}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    stop = ["\n", " Human:", ]
    corrected_text = response.choices[0].text.strip()
    speak(corrected_text)


def dall_e():
    global num
    num += 1
    query = takeCommand().lower()
    response = openai.Image.create(
        prompt=str(query),
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(f"DALL-E Image URL: {image_url}")
    


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("GOOD MORNING")

    elif 12 <= hour < 15:
        speak("GOOD AFTERNOON")

    elif 15 <= hour < 19:
        speak("GOOD Evening")

    else:
        speak("hello!")

    speak("Jarvis at your service sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(f"Error: {e}")
        print("Say that again please")
        return "None"
    return query


if __name__ == '__main__':
    num = 1
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'sarcasm' in query:
            sarcasm()
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'generate the commanded image' in query:
            dall_e()
        elif 'correct the grammar' in query:
            grammar_correction()
        elif  'who is pranav' in  query:
            speak(f'He is the legend.  Firstranker and genius who has created me')
        
        elif 'the prime minister of india' in query:
            speak(f'the prime minister if india is narendra modi ')

        elif 'the president of india' in query:
            speak(f'the president of india is draupadi murmu')

        elif 'the prime minister of britain' in query:
            speak(f'the prime minister of britain is rishi sunak')
        elif 'the chief minister of telangana' in query:
            speak(f'Revanth reddy is the chief minister of telangana')

        
        
        elif  'who is yogi adityanath' in  query:
            speak(f'he is the gem of the century')

        elif 'open google' in query:
            speak(f"On your command pranav sir")
            
            webbrowser.open("google.com")

        elif 'hukum songs' in query:
             speak(f"On your command sir")
            
             webbrowser.open("www.youtube.com/watch?v=1F3hm6MfR1k")
            

        elif 'open youtube' in query:
             speak(f"On your command. sir")
            
             webbrowser.open("youtube.com")


        elif 'play salaar songs' in query:
             speak(f"On your command sir")
            
             webbrowser.open("www.youtube.com/watch?v=7QjFV85RVEE")

        elif 'open maps' in query:
             speak(f"On your command. sir")
            
             webbrowser.open("www.google.com/maps")

        

        elif 'open code' in query:
           speak(f"On your command. sir")
           codePath="C:\\Users\\ACER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'what are you capable of' in query:
            speak(f'i am capable of running cars without human intervention. build smart cities. help people in their chores and keep the entire ecosystem safe and balanced')
        
        elif 'who are you' in query:
            speak(f'i am an advanced automated artificial intelligence system capable of running cars on my fingertips without human intervention too')
        
        
        
        elif 'what is the weather' in query:
            speak(f'working on it sir')
            webbrowser.open("www.accuweather.com/en/in/hyderabad/202190/weather-forecast/202190")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        elif 'who is prabhas' in query:
             speak(f"he is the most famous and one of the highest paid stars in india with several blockbusters and highest fan following. his upcoming movie. salaar is predicted to earn over 2000 crores emerging as the biggest blockbuster of all time")
        
        

       
        
        
        

    

        
      





