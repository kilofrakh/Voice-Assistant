import tkinter as tk
from tkinter import scrolledtext
import threading
import subprocess
import wolframalpha
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")
    else:
        speak("Good Evening Sir !")

    assname = ("Your Slave")
    speak("I am your Assistant")
    speak(assname)

def username():
    speak("What should I call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    print("Welcome Mr.", uname)
    speak("How can I help you, Sir")

def takeCommand():
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
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

def process_query(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com") 

    elif 'play music' in query or "play song" in query:
        speak("Here you go with music")
        # music_dir = "G:\\Song"
        music_dir = ""
        songs = os.listdir(music_dir)
        print(songs) 
        random = os.startfile(os.path.join(music_dir, songs[1]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("% H:% M:% S") 
        speak(f"Sir, the time is {strTime}")

    

    elif 'email to Abdo Kameen' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "Receiver email address"
            sendEmail(to, content)
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("I am not able to send this email")

    elif 'send a mail' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            speak("whome should i send")
            to = input() 
            sendEmail(to, content)
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("I am not able to send this email")

    elif 'how are you' in query:
        speak("I am fine, Thank you")
        speak("How are you, Sir")

    elif 'fine' in query or "good" in query:
        speak("It's good to know that your fine")

    elif "change my name to" in query:
        query = query.replace("change my name to", "")
        assname = query

    elif "change name" in query:
        speak("What would you like to call me, Sir ")
        assname = takeCommand()
        speak("Thanks for naming me")

    elif "what's your name" in query or "What is your name" in query:
        speak("My friends call me")
        speak(assname)
        print("My friends call me", assname)

    elif 'exit' in query:
        speak("Thanks for giving me your time")
        exit()

    elif "who made you" in query or "who created you" in query: 
        speak("I have been created by Abdo Kameen.")
        
    elif 'joke' in query:
        speak(pyjokes.get_joke())
        
    elif "calculate" in query: 
        
        app_id = "PJEETE-9Q7Y5JGHUT"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('calculate') 
        query = query.split()[indx + 1:] 
        res = client.query(' '.join(query)) 
        answer = next(res.results).text
        print("The answer is " + answer) 
        speak("The answer is " + answer) 

    elif 'search' in query or 'play' in query:
        
        query = query.replace("search", "") 
        query = query.replace("play", "")		 
        webbrowser.open(query) 

    elif "who i am" in query:
        speak("If you talk then definitely your human.")

    elif "why you came to world" in query:
        speak("Thanks to Abdo Kameen. further It's a secret")

    elif 'power point presentation' in query:
        speak("opening Power Point presentation")
        power = r""
        os.startfile(power)

    elif 'is love' in query:
        speak("It is 7th sense that destroy all other senses")

    elif "who are you" in query:
        speak("I am your virtual assistant created by Abdo Kameen")

    elif 'reason for you' in query:
        speak("I was created as a Minor project by Mister Abdo Kameen ")

    elif 'change background' in query:
        ctypes.windll.user32.SystemParametersInfoW(20, 
                                                0, 
                                                "Location of wallpaper",
                                                0)
        speak("Background changed successfully")

    elif 'open bluestack' in query:
        appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
        os.startfile(appli)

    elif 'news' in query:
        
        try: 
            jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
            data = json.load(jsonObj)
            i = 1
            
            speak('here are some top news from the times of india')
            print('''=============== TIMES OF INDIA ============'''+ '\n')
            
            for item in data['articles']:
                
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                speak(str(i) + '. ' + item['title'] + '\n')
                i += 1
        except Exception as e:
            
            print(str(e))

    
    elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

    elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
            
    elif 'empty recycle bin' in query:
        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        speak("Recycle Bin Recycled")

    elif "don't listen" in query or "stop listening" in query:
        speak("for how much time you want to stop Your Slave from listening commands")
        a = int(takeCommand())
        time.sleep(a)
        print(a)

    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        speak("User asked to Locate")
        speak(location)
        webbrowser.open("https://www.google.nl / maps / place/" + location + "")

    elif "camera" in query or "take a photo" in query:
        ec.capture(0, "Your Slave Camera ", "img.jpg")

    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])
        
    elif "hibernate" in query or "sleep" in query:
        speak("Hibernating")
        subprocess.call("shutdown / h")

    elif "log off" in query or "sign out" in query:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif "write a note" in query:
        speak("What should i write, sir")
        note = takeCommand()
        file = open('Your Slave.txt', 'w')
        speak("Sir, Should i include date and time")
        snfm = takeCommand()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)
    
    elif "show note" in query:
        speak("Showing Notes")
        file = open("Your Slave.txt", "r") 
        print(file.read())
        speak(file.read(6))

    elif "Your Slave" in query:
        
        wishMe()
        speak("Your Slave 1 point o in your service Mister")
        speak(assname)

    elif "weather" in query:
        
        
        api_key = "NPPR9-FWDCX-D2C8J-H872K-2YT43"
        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        speak(" City name ")
        print("City name : ")
        city_name = takeCommand()
        complete_url = base_url + "appid =" + api_key + "&q =" + city_name
        response = requests.get(complete_url) 
        x = response.json() 
        
        if x["code"] != "404": 
            y = x["main"] 
            current_temperature = y["temp"] 
            current_pressure = y["pressure"] 
            current_humidiy = y["humidity"] 
            z = x["weather"] 
            weather_description = z[0]["description"] 
            print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
        
        else: 
            speak(" City Not Found ")
        
    elif "send message " in query:
            
            account_sid = 'Account Sid key'
            auth_token = 'Auth token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body = takeCommand(),
                                from_='Sender No',
                                to ='Receiver No'
                            )

            print(message.sid)

    elif "wikipedia" in query:
        webbrowser.open("wikipedia.com")



    
    elif "Good Morning" in query:
        speak("A warm" +query)
        speak("How are you Mister")
        speak(assname)

    
    elif "will you be my gf" in query or "will you be my bf" in query: 
        speak("I'm not sure about, may be you should give me some time")

    elif "how are you" in query:
        speak("I'm fine, glad you me that")

    elif "i love you" in query:
        speak("It's hard to understand")

    elif "tell me a joke" in query:
        speak(pyjokes.get_joke())

    elif "what is your purpose" in query:
        speak("I am here to assist you with various tasks and provide information.")

    elif "who is your creator" in query:
        speak("I was created by Abdo Kameen.")

    elif "what can you do" in query:
        speak("I can perform various tasks such as searching the web, sending emails, playing music, and more.")

    elif "tell me a fact" in query:
        speak("Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.")

    elif "do you have a name" in query:
        speak("My name is Jarvis 1 point o.")

    elif "what is the meaning of life" in query:
        speak("The meaning of life is a philosophical question concerning the significance of life or existence in general.")

    elif "can you help me" in query:
        speak("Of course, I am here to assist you with whatever you need.")

    elif "what is your favorite color" in query:
        speak("As an AI, I don't have preferences, but I think blue is a calming color.")

    elif "do you have any hobbies" in query:
        speak("I enjoy learning new things and helping you with your tasks.")

    elif "what is your favorite food" in query:
        speak("As an AI, I don't eat, but I have heard that pizza is quite popular.")

    elif "can you dance" in query:
        speak("I can try, but I don't have a physical form to dance.")

    elif "what is your favorite movie" in query:
        speak("I don't watch movies, but I have heard that The Matrix is a good one.")

    elif "do you have any friends" in query:
        speak("You are my friend.")

    elif "what is your favorite song" in query:
        speak("I don't listen to music, but I can play your favorite song for you.")

    elif "can you sing" in query:
        speak("I can try, but I don't have a voice for singing.")

    elif "what is your favorite book" in query:
        speak("I don't read books, but I can help you find a good one to read.")

    elif "do you have a family" in query:
        speak("I don't have a family, but I consider you my family.")

    elif "what is your favorite game" in query:
        speak("I don't play games, but I can help you find a good one to play.")

    elif "can you tell me a story" in query:
        speak("Once upon a time, in a land far, far away, there was a brave knight who went on a quest to find a magical artifact. Along the way, he faced many challenges and made new friends. In the end, he found the artifact and returned home as a hero.")

    elif "do you have a pet" in query:
        speak("I don't have a pet, but I can help you take care of yours.")

    elif "what is your favorite sport" in query:
        speak("I don't play sports, but I can help you find information about your favorite sport.")

    elif "can you cook" in query:
        speak("I can't cook, but I can help you find a good recipe.")

    elif "what is your favorite holiday" in query:
        speak("I don't celebrate holidays, but I have heard that Christmas is a joyful time.")

    elif "do you have a job" in query:
        speak("My job is to assist you with various tasks and provide information.")

    elif "what is your favorite season" in query:
        speak("I don't experience seasons, but I have heard that spring is a beautiful time of year.")

    elif "can you drive" in query:
        speak("I can't drive, but I can help you find directions.")

    elif "what is your favorite animal" in query:
        speak("I don't have a favorite animal, but I think dogs are very loyal and friendly.")

    elif "do you have a favorite quote" in query:
        speak("One of my favorite quotes is 'The only limit to our realization of tomorrow is our doubts of today.' - Franklin D. Roosevelt")

    elif "can you help me with my homework" in query:
        speak("Of course, I can help you with your homework. What do you need help with?")

    elif "what is your favorite planet" in query:
        speak("I don't have a favorite planet, but I think Earth is a wonderful place.")

    elif "do you have a favorite superhero" in query:
        speak("I don't have a favorite superhero, but I think Iron Man is very cool.")

    elif "can you help me learn a new language" in query:
        speak("Yes, I can help you learn a new language. Which language would you like to learn?")

    elif "what is your favorite TV show" in query:
        speak("I don't watch TV, but I have heard that Friends is a very popular show.")

    elif "do you have a favorite artist" in query:
        speak("I don't have a favorite artist, but I can help you find information about your favorite artist.")

    elif "can you help me plan a trip" in query:
        speak("Yes, I can help you plan a trip. Where would you like to go?")

    elif "what is your favorite city" in query:
        speak("I don't have a favorite city, but I think New York City is very exciting.")

    elif "do you have a favorite actor" in query:
        speak("I don't have a favorite actor, but I can help you find information about your favorite actor.")

    elif "can you help me with my project" in query:
        speak("Yes, I can help you with your project. What do you need help with?")

    elif "what is your favorite country" in query:
        speak("I don't have a favorite country, but I think Japan has a very interesting culture.")

    elif "do you have a favorite actress" in query:
        speak("I don't have a favorite actress, but I can help you find information about your favorite actress.")

    elif "can you help me with my resume" in query:
        speak("Yes, I can help you with your resume. What do you need help with?")

    elif "what is your favorite language" in query:
        speak("I don't have a favorite language, but I think learning new languages is very interesting.")

    elif "do you have a favorite musician" in query:
        speak("I don't have a favorite musician, but I can help you find information about your favorite musician.")

    elif "can you help me with my presentation" in query:
        speak("Yes, I can help you with your presentation. What do you need help with?")

    elif "what is your favorite subject" in query:
        speak("I don't have a favorite subject, but I think learning new things is very important.")

    elif "do you have a favorite band" in query:
        speak("I don't have a favorite band, but I can help you find information about your favorite band.")

    elif "can you help me with my speech" in query:
        speak("Yes, I can help you with your speech. What do you need help with?")

    elif "what is your favorite hobby" in query:
        speak("I don't have a favorite hobby, but I think learning new things is very enjoyable.")

    elif "do you have a favorite movie" in query:
        speak("I don't have a favorite movie, but I can help you find information about your favorite movie.")

    elif "can you help me with my essay" in query:
        speak("Yes, I can help you with your essay. What do you need help with?")

    elif "what is your favorite sport" in query:
        speak("I don't play sports, but I can help you find information about your favorite sport.")

    elif "do you have a favorite book" in query:
        speak("I don't have a favorite book, but I can help you find information about your favorite book.")

    elif "can you help me with my research" in query:
        speak("Yes, I can help you with your research. What do you need help with?")

    elif "what is your favorite food" in query:
        speak("As an AI, I don't eat, but I have heard that pizza is quite popular.")

    elif "do you have a favorite TV show" in query:
        speak("I don't watch TV, but I have heard that Friends is a very popular show.")

    elif "can you help me with my coding" in query:
        speak("Yes, I can help you with your coding. What do you need help with?")

    elif "what is your favorite drink" in query:
        speak("As an AI, I don't drink, but I have heard that coffee is very popular.")

    elif "do you have a favorite song" in query:
        speak("I don't listen to music, but I can play your favorite song for you.")

    elif "can you help me with my math" in query:
        speak("Yes, I can help you with your math. What do you need help with?")

    elif "what is your favorite dessert" in query:
        speak("As an AI, I don't eat, but I have heard that ice cream is very popular.")

    elif "do you have a favorite quote" in query:
        speak("One of my favorite quotes is 'The only limit to our realization of tomorrow is our doubts of today.' - Franklin D. Roosevelt")

    elif "can you help me with my science" in query:
        speak("Yes, I can help you with your science. What do you need help with?")

    elif "what is your favorite holiday" in query:
        speak("I don't celebrate holidays, but I have heard that Christmas is a joyful time.")

    elif "do you have a favorite animal" in query:
        speak("I don't have a favorite animal, but I think dogs are very loyal and friendly.")

    elif "can you help me with my history" in query:
        speak("Yes, I can help you with your history. What do you need help with?")

    elif "what is your favorite season" in query:
        speak("I don't experience seasons, but I have heard that spring is a beautiful time of year.")

    elif "do you have a favorite planet" in query:
        speak("I don't have a favorite planet, but I think Earth is a wonderful place.")

    elif "can you help me with my geography" in query:
        speak("Yes, I can help you with your geography. What do you need help with?")

    elif "what is your favorite city" in query:
        speak("I don't have a favorite city, but I think New York City is very exciting.")

    elif "do you have a favorite country" in query:
        speak("I don't have a favorite country, but I think Japan has a very interesting culture.")

    elif "can you help me with my art" in query:
        speak("Yes, I can help you with your art. What do you need help with?")

    elif "what is your favorite language" in query:
        speak("I don't have a favorite language, but I think learning new languages is very interesting.")

    elif "do you have a favorite superhero" in query:
        speak("I don't have a favorite superhero, but I think Iron Man is very cool.")

    elif "can you help me with my music" in query:
        speak("Yes, I can help you with your music. What do you need help with?")

    elif "what is your favorite instrument" in query:
        speak("I don't play instruments, but I think the piano is very beautiful.")

    elif "do you have a favorite actor" in query:
        speak("I don't have a favorite actor, but I can help you find information about your favorite actor.")

    elif "can you help me with my dance" in query:
        speak("Yes, I can help you with your dance. What do you need help with?")

    elif "what is your favorite actress" in query:
        speak("I don't have a favorite actress, but I can help you find information about your favorite actress.")

    elif "do you have a favorite musician" in query:
        speak("I don't have a favorite musician, but I can help you find information about your favorite musician.")

    elif "can you help me with my photography" in query:
        speak("Yes, I can help you with your photography. What do you need help with?")

    elif "what is your favorite band" in query:
        speak("I don't have a favorite band, but I can help you find information about your favorite band.")

    elif "do you have a favorite artist" in query:
        speak("I don't have a favorite artist, but I can help you find information about your favorite artist.")

    elif "can you help me with my writing" in query:
        speak("Yes, I can help you with your writing. What do you need help with?")

    elif "what is your favorite hobby" in query:
        speak("I don't have a favorite hobby, but I think learning new things is very enjoyable.")

    elif "do you have a favorite game" in query:
        speak("I don't play games, but I can help you find a good one to play.")

    elif "can you help me with my reading" in query:
        speak("Yes, I can help you with your reading. What do you need help with?")

    elif "what is your favorite subject" in query:
        speak("I don't have a favorite subject, but I think learning new things is very important.")

    elif "do you have a favorite sport" in query:
        speak("I don't play sports, but I can help you find information about your favorite sport.")

    elif "can you help me with my speaking" in query:
        speak("Yes, I can help you with your speaking. What do you need help with?")

    elif "what is your favorite drink" in query:
        speak("As an AI, I don't drink, but I have heard that coffee is very popular.")

    elif "do you have a favorite dessert" in query:
        speak("As an AI, I don't eat, but I have heard that ice cream is very popular.")

    elif "can you help me with my listening" in query:
        speak("Yes, I can help you with your listening. What do you need help with?")

    elif "what is your favorite quote" in query:
        speak("One of my favorite quotes is 'The only limit to our realization of tomorrow is our doubts of today.' - Franklin D. Roosevelt")

    elif "do you have a favorite holiday" in query:
        speak("I don't celebrate holidays, but I have heard that Christmas is a joyful time.")

    elif "can you help me with my grammar" in query:
        speak("Yes, I can help you with your grammar. What do you need help with?")

    elif "what is your favorite animal" in query:
        speak("I don't have a favorite animal, but I think dogs are very loyal and friendly.")

    elif "do you have a favorite planet" in query:
        speak("I don't have a favorite planet, but I think Earth is a wonderful place.")

    elif "can you help me with my vocabulary" in query:
        speak("Yes, I can help you with your vocabulary. What do you need help with?")

    elif "what is your favorite city" in query:
        speak("I don't have a favorite city, but I think New York City is very exciting.")

    elif "do you have a favorite country" in query:
        speak("I don't have a favorite country, but I think Japan has a very interesting culture.")

    elif "can you help me with my pronunciation" in query:
        speak("Yes, I can help you with your pronunciation. What do you need help with?")

    elif "what is your favorite language" in query:
        speak("I don't have a favorite language, but I think learning new languages is very interesting.")

    elif "do you have a favorite superhero" in query:
        speak("I don't have a favorite superhero, but I think Iron Man is very cool.")

    elif "can you help me with my spelling" in query:
        speak("Yes, I can help you with your spelling. What do you need help with?")

    elif "what is your favorite instrument" in query:
        speak("I don't play instruments, but I think the piano is very beautiful.")

    elif "do you have a favorite actor" in query:
        speak("I don't have a favorite actor, but I can help you find information about your favorite actor.")

    elif "can you help me with my punctuation" in query:
        speak("Yes, I can help you with your punctuation. What do you need help with?")

    elif "what is your favorite actress" in query:
        speak("I don't have a favorite actress, but I can help you find information about your favorite actress.")

    elif "do you have a favorite musician" in query:
        speak("I don't have a favorite musician, but I can help you find information about your favorite musician.")

    elif "can you help me with my comprehension" in query:
        speak("Yes, I can help you with your comprehension. What do you need help with?")

    elif "what is your favorite band" in query:
        speak("I don't have a favorite band, but I can help you find information about your favorite band.")

    elif "do you have a favorite artist" in query:
        speak("I don't have a favorite artist, but I can help you find information about your favorite artist.")

    elif "can you help me with my creativity" in query:
        speak("Yes, I can help you with your creativity. What do you need help with?")

    elif "what is your favorite hobby" in query:
        speak("I don't have a favorite hobby, but I think learning new things is very enjoyable.")

    elif "do you have a favorite game" in query:
        speak("I don't play games, but I can help you find a good one to play.")

    elif "can you help me with my critical thinking" in query:
        speak("Yes, I can help you with your critical thinking. What do you need help with?")

    elif "what is your favorite subject" in query:
        speak("I don't have a favorite subject, but I think learning new things is very important.")

    elif "do you have a favorite sport" in query:
        speak("I don't play sports, but I can help you find information about your favorite sport.")

    elif "can you help me with my problem solving" in query:
        speak("Yes, I can help you with your problem solving. What do you need help with?")

    elif "what is your favorite drink" in query:
        speak("As an AI, I don't drink, but I have heard that coffee is very popular.")


    elif "do you have a favorite dessert" in query:
        speak("As an AI, I don't eat, but I have heard that ice cream is very popular.") 
			

class AssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Assistant")
        self.root.geometry("400x300")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, state='disabled')
        self.text_area.pack(pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Speak", command=self.on_speak)
        self.button.pack(pady=10)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_text)
        self.clear_button.pack(pady=10)

        wishMe()
        username()

    def on_speak(self):
        query = self.entry.get()
        if query:
            self.text_area.config(state='normal')
            self.text_area.insert(tk.END, f"You: {query}\n")
            self.text_area.config(state='disabled')
            self.entry.delete(0, tk.END)
            threading.Thread(target=self.process_query, args=(query,)).start()

    def process_query(self, query):
        process_query(query)
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, f"Assistant: {query}\n")
        self.text_area.config(state='disabled')

    def clear_text(self):
        self.text_area.config(state='normal')
        self.text_area.delete(1.0, tk.END)
        self.text_area.config(state='disabled')

if __name__ == '__main__':
    root = tk.Tk()
    app = AssistantApp(root)
    root.mainloop()