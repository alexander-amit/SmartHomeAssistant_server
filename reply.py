# execute following command:
# pip install PySpeech 
# pip install PyAudio
# pip install pyttsx3
# pip install sr
# pip install SpeechRecognition

import pyttsx3

        
def reply(msg): 
        engine = pyttsx3.init()
        engine.say(msg)
        engine.runAndWait()
    