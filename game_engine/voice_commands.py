# voice_commands.py

import speech_recognition as sr

class VoiceCommands:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_for_command(self):
        with self.microphone as source:
            print("Listening for command...")
            audio = self.recognizer.listen(source)
        try:
            command = self.recognizer.recognize_google(audio)
            print(f"Command recognized: {command}")
            return command
        except sr.UnknownValueError:
            print("Could not understand the command")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
            return None

    def process_command(self, command, game_state):
        # Add logic to process and execute voice commands
        if command:
            print(f"Processing command: {command}")
            # Example: command could be "attack with all" or "play card"
            if "attack" in command:
                game_state.current_player.attack_with_all()
            elif "play" in command:
                # Extract card name from command
                card_name = command.replace("play ", "")
                game_state.current_player.play_card(card_name)
