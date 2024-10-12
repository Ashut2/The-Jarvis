import speech_recognition as sr
import webbrowser
import pyttsx3
# from pocketsphinx import Decoder

recognizer = sr.Recognizer()
engine = pyttsx3.init() # initializes the ttsx3 module

def speak(text):
    engine.say(text)
    engine.runAndWait()

def procces_camand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    if "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    if "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    if "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    if "open canva" in c.lower():
        webbrowser.open("https://canva.com")
    # if "open google sheet" in c.lower():
    #     webbrowser.open("docs.google.com")
    # print(c)

if __name__ == "__main__":
    speak("Initialising Jarvis")
    while True :
        # listen for the vague word "jarvis"
        # obtain asudio from the microphone 
        r = sr.Recognizer()
        
        # recognize speech using Sphinx
        
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=1,phrase_time_limit=0)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Your Smart Jarvis Ai Assistant activated ...")
            # if(word.lower() == " hey jarvis"):
            #     speak("Your Smart Jarvis Ai Assistant activated ... how may i help you sir")
            # if(word.lower() == " hi jarvis"):
            #     speak("Your Smart Jarvis Ai Assistant activated ... how may i help you sir")
            # if(word.lower() == " hello jarvis"):
            #     speak("Your Smart Jarvis Ai Assistant activated ... how may i help you sir")
                
                # listening for command 

                with sr.Microphone() as source:
                   print("Jarvis Activated...")
                   audio = r.listen(source,timeout=1,phrase_time_limit=0)
                command = r.recognize_google(audio)
            
                procces_camand(command)

            # print(command)
        except Exception as e:
           print("error; {0}".format(e))