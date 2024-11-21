import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
# from pocketsphinx import Decoder

recognizer = sr.Recognizer()
engine = pyttsx3.init() # initializes the ttsx3 module

def speak(text):
    engine.say(text)
    engine.runAndWait()

# adding task management functionality
def add_task_via_jarvis(task):
    response = requests.post('http://127.0.0.1:5000/add-task', json={"task": task})
    return response.json().get("message", "Failed to add task.")

def get_tasks_via_jarvis():
    response = requests.get('http://127.0.0.1:5000/get-tasks')
    tasks = response.json().get("tasks", [])
    return tasks

# def remove_task_via_jarvis(task):
#     response = requests.post('http://127.0.0.1:5000/delete-task', json={"task": task})
#     return response.json().get("message", "Failed to delete task.")



# error handling code for wrong api response via jarvis 

def remove_task_via_jarvis(task):
    try:
        response = requests.post('http://127.0.0.1:5000/delete-task', json={"task": task})
        response.raise_for_status()  # Raises an error for HTTP error responses
        return response.json().get("message", "Failed to delete task.")
    except requests.exceptions.RequestException as e:
        print("Error with the delete task request:", e)
        return "Could not connect to the task manager."
    except ValueError:
        print("Error: Received an empty or malformed response from the server.")
        return "Error in deleting the task due to server response."



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
    if "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "add task" in c.lower():
        task = c.lower().replace("add task","")
        result = add_task_via_jarvis(task)
        speak(result)
    elif "get task" in c.lower():
        tasks = get_tasks_via_jarvis()
        if tasks:
            for t in tasks:
                speak("your task are ")
                speak(t)
        else:
            speak("you have no tasks.")

    elif "remove task" in c.lower():
        task = c.lower().replace("remove task","")
        result = remove_task_via_jarvis(task)
        speak(result)
    
    else:
        speak("commmand not recognized.")
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
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak(" Smart Jarvis  Assistant activated , now speak ...")
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
                print(f"command = {command}")
                procces_camand(command)

            # print(command)
        except Exception as e:
           print("error; {0}".format(e))