import pyttsx3 #for voice processing

#root variables
Designation = "sir"
Name = "Jarvis"
version = "1.5.0"
speed_of_speaking = 170
volume = 0.5
male_female_voice = 0 #0 for David voice and #1 for Mark voice #2 for Zira 

Jarvis = pyttsx3.init('sapi5')
voices = Jarvis.getProperty('voices')
# print(voices)
Jarvis.setProperty('voice', voices[male_female_voice].id)
Jarvis.setProperty('rate', speed_of_speaking)
Jarvis.setProperty('volume', volume)

def speak(audio):
    Jarvis.say(audio)
    Jarvis.runAndWait()


speak("Hello world")