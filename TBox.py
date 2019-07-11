## Libraries
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
#import music_api
import requests

class Jarvis:

    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    def speak(self, audio):
        #This is responsible for audio
        self.engine.say(audio)
        self.engine.runAndWait()
        try:
            requests.post('http://arctecindia.com/TBox/query.php?data=' + '\n\n')
        except requests.exceptions.ConnectionError:
            self.engine.say("Internet Connection Not Available, Try Again Later.")
            self.engine.runAndWait()
            exit()

    def introduce(self):
        self.speak("I am TBox, Sir. Please tell me how may I help you")

    def wishMe(self):
        #This wishes according to the time.
        
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.speak("Good Morning!")

        elif hour>=12 and hour<18:
            self.speak("Good Afternoon!")   

        else:
            self.speak("Good Evening!")  
        
        self.introduce()

        

    def takeCommand(self):
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            # r.energy_threshold = 1000
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            requests.post('http://arctecindia.com/TBox/query.php?data=' + query)

        except Exception as e:
            print(e)    
            print("Say that again please...")  
            return ''
        return query

    # def SpotifyFetch(self):
    #     stuff = music_api.Spotify()
    #     self.speak(stuff[1])
    #     self.speak(stuff[2])
    #     self.speak(stuff[0])
        
    def queryExecution(self, query):
        # Logic for executing tasks based on query
        
        if 'wikipedia' in query:
            self.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            self.speak("According to Wikipedia")
            print(results)
            self.speak(results)

        elif 'open youtube' in query:
            self.speak('Opening Youtube...')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            self.speak('Opening Google...')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            self.speak('Opening Stack Overflow...')
            webbrowser.open("stackoverflow.com")
        
        elif 'exit' in query:
            requests.post('http://arctecindia.com/TBox/query.php?data=' + '\n\n')
            exit()


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            self.speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Aaditya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to addy' in query:
            try:
                self.speak("What should I say?")
                content = self.takeCommand()
                to = "addyrockx96@gmail.com"    
                self.sendEmail(to, content)
                self.speak("Email has been sent!")
            except Exception as e:
                print(e)
                self.speak("Unable to Send")
        
        '''
        elif 'what is playing' in query:
            try:
                self.SpotifyFetch()
            except Exception as e:
                print(e)
                self.speak('Nothing is Playing')
        '''


    def sendEmail(self, to, content):
        #It sends the mail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.wishMe()
    
    while True:
        query = jarvis.takeCommand().lower()
        jarvis.queryExecution(query)

        

