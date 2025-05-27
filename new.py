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

    import pyautogui

# Press a key
pyautogui.press('space')  # Press the spacebar

# Type a string

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon, QFont
import google.generativeai as genai

# Step 2: Main Game Loop.
def main():
  pet_name = input("Name your Maggotchi:")
  pet = Maggotchi(pet_name)

  while True:
      pet.status()
      print("\nIt still is breathing. What will you do?")
      print("1. Sicken it.")
      print("2. Fend it off.")
      print("3. Sense danger.")
      print("4. Quit.")

      choice = input("Enter your choice (1-4): ")

      if choice == "1":
        pet.sicken()
      elif choice == "2":
        pet.fendoff()
      elif choice == "3":
        pet.sensedanger()
      elif choice == "4":
        print(f"Goodbye, {pet.name}...!")
        break
      else:
        print("Invalid choice. Please try again.")

    # Ensure attributes stay within bounds.
      pet.ImmuneEvasion = max(0, min(100, pet.ImmuneEvasion))
      pet.FeedingMechanism = max(0, min(100, pet.FeedingMechanism))
      pet.ReproductiveOutput = max(0, min(100, pet.ReproductiveOutput))

      # Introduce random events occasionally
      if random() < 0.3:  # 30% chance of a random event occurring
        pet.random_event()

        # Check pet's well-being
      if pet.hunger >= 100:
        print(f"{pet.name} survived, the poison didn't do the trick! Game over.")
        break
      if pet.happiness <= 0:
        print(f"{pet.name} ate, the artery has been torn! Game over.")
        break
      if pet.energy <= 0:
        print(f"{pet.name} bore, the offspring escaped the bunker! Game over.")
        break

if __name__ == "__main__":
  main()