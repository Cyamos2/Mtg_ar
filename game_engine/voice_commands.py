import speech_recognition as sr

def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Listening for your command...")
    with microphone as source:
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return None
