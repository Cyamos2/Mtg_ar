# game_engine/voice_commands.py

import speech_recognition as sr

class VoiceCommands:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_command(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
            try:
                return self.recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                return "Sorry, I did not understand that."
            except sr.RequestError:
                return "Sorry, my speech service is down."
