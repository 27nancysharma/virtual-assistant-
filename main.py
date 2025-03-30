
import speech_recognition as sr 
import webbrowser
import pyttsx3
import musicLibrary
import os
import requests



recognizer= sr.Recognizer()
engine = pyttsx3.init()
newsapi ="33b133ee17354bb0be1140af296f2b1c"

def speak(text):
    engine.say( text)
    engine.runAndWait()
    
    
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://in.linkedin.com/")
    elif "open spofify" :
        os.system("start spotify")
    elif "open whatsapp":
        os.system("start whatsapp")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link =musicLibrary.music[song]
        webbrowser.open(link)   
        
        
    elif "news"in c.lower().startswith("news"):
       r  =  requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            
            data =r.json()
            
            articles=data.get('articles',[])
            
            for articles in articles:
                speak(articles['title'])
                
    else:
        # let openAI handle the request



if __name__ == "__main__" :
    speak("initilizing jarvis....")
    while True:
     # listening for the word "jarvis"
     # obtain audio from the microphone
        r = sr.Recognizer()
           
     # recognize speech using google
     
        print("recognozing...") 
        try:
            with sr.Microphone() as source:
               print("listening....")
               audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word= r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                 speak("ya")
             #  listen for command
                 with sr.Microphone() as source:
                     print("jarvis active....")
                     audio = r.listen(source)
                     command= r.recognize_google(audio)
                 
                 processcommand(command)
                 
                 
        except Exception as e:
            print("error; {0}".format(e))
    
    