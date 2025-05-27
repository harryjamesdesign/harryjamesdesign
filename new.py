from datetime import datetime
import pyttsx3
import speech_recognition as sr

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen_to_user():
    with sr.Microphone() as mic:
        print("Assistant: I am listening...")
        try:
            audio = recognizer.listen(mic)
            user_input = recognizer.recognize_google(audio).lower()
            print("You said:", user_input)
            return user_input
        except sr.UnknownValueError:
            print("I didn't catch that. Please try again.")
        except sr.RequestError:
            print("Sorry, the speech service is unavailable.")
        return ""

def generate_response(user_input, user_name):
    now = datetime.now()

    if user_input == "":
        return "I can't hear you, try again?"
    elif "hello" in user_input:
        return f"Hello, {user_name}!"
    elif "how are you" in user_input:
        return "I'm fine, thank you!"
    elif "date" in user_input and "time" not in user_input:
        return f"Today's date is: {now.strftime('%d/%m/%Y')}"
    elif "time" in user_input:
        return f"Current time is: {now.strftime('%H:%M:%S')}"
    elif "bye" in user_input or "goodbye" in user_input:
        return f"Goodbye, {user_name}!"
    else:
        return "I'm not sure how to respond to that."

def speak_response(response):
    print("Assistant:", response)
    tts_engine.say(response)
    tts_engine.runAndWait()

def main():
    user_name = input("What is your name?").strip()
    print(f"Hi, {user_name}")
    
    while True:
        user_input = listen_to_user()
        response = generate_response(user_input, user_name)

        speak_response(response)        

        if "bye" in user_input or "goodbye" in user_input:
            break

if __name__ == "__main__":
    main()