import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()   # Help to recognize the speech
   # pyttsx initilize ho jayga

def speak (text):
    engine = pyttsx3.init()  
    engine.say (text)
    engine.runAndWait()
    # engine.stop()

def processcommand(c):
    print(c)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    
    # Listen to the wake up word 'Jarvis' then collect audio grom microphone
    while True:
        r = sr.Recognizer()
        
        # recognize speech using Sphinx
        print("recorgnizing...")
        try:
           with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
           word = r.recognize_google(audio)

           if(word.lower() == "jarvis"):
               speak("Yaa...")
               # Listen for command
               with sr.Microphone() as source:
                    print("Jarvis Active!")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
