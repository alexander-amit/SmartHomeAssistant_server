# execute following command:
# pip install PySpeech 
# pip install PyAudio
# pip install pyttsx3
# pip install sr
# pip install SpeechRecognition

import speech_recognition as sr
import pyttsx3

        
def takeOrder(): 
    #engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        #engine.runAndWait()
        audio = r.listen(source)
    try:
        saidbyme=r.recognize_google(audio)
        print("I thinks you said " + saidbyme)
        engine = pyttsx3.init()
        engine.say("I thinks you said " + saidbyme)
        
        engine.runAndWait()
        return saidbyme
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "none"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "none"