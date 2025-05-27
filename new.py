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

  from random import choice, random
EVENTS = [
    ("The parasite begins to supress the host's immune system. You get the syringe.",
      0, 10, 0),
    ("The parasite begins to obtain nutrients from the host. You can feel the teeth.",
      -10, 0, 0),
    ("The parasite bore offspring. You manage to cook most of it.", 0, -10,
      0),
    ("The parasite inhaled the toxins and lost energy. You sigh in ease.", 0,
      0, -10)
]

class Maggotchi:

  def __init__(self, name):
    self.name = name
    self.ImmuneEvasion = 50
    self.FeedingMechanism = 50
    self.ReproductiveOutput = 50

  def sicken(self):
    self.ImmuneEvasion -= 10
    self.FeedingMechanism += 5
    print(f"{self.name} has been sickened. That doesn't stop hunger.")

  def fendoff(self):
    self.FeedingMechanism += 10
    self.ReproductiveOutput -= 10
    print(f"{self.name} feeds on you. You fend it off.")

  def adaption(self):
    self.ReproductiveOutput += 10
    self.FeedingMechanism += 5
    print(f"{self.name} is adapted to it's new environment. It's reproducing.")

  def status(self):
    print(f"{self.name}'s Status - ImmuneEvasion: {self.ImmuneEvasion}")
    print(f"FeedingMechanism: {self.FeedingMechanism}")
    print(f"ReproductiveOutput: {self.ReproductiveOutput}")
  
  def random_event(self):
    event = choice(EVENTS)
    print(f"{self.name} {event[0]}")
    self.ImmuneEvasion += event[1]
    self.FeedingMechanism += event[2]
    self.ReproductiveOutput += event[3]

    #Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
#nr_symbols = int(input(f"How many symbols would you like?\n"))
#nr_numbers = int(input(f"How many numbers would you like?\n"))

sublist_letter = letters[0:52]
sublist_num = numbers[0:10]
sublist_sym = symbols[0:9]

let_count = 0
rand_letter = ""
for letc in letters:
    rand_letter += random.choice(sublist_letter)
    let_count += 1
    if let_count > nr_letters:
        break

print(rand_letter)

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("b is less than a")

  class TicketCategory(discord.ui.Select):
    def __init__(self, bot):
        with open('Configurations/TicketModule.json', encoding='utf-8-sig') as f:
            data = json.load(f)
        options = []
        for category, details in data['TICKET_CATEGORIES'].items():
            emoji = details['Emoji'] # Right here
            options.append(SelectOption(label=category, value=category, emoji=emoji))
        super().__init__(placeholder="Select a ticket category...", min_values=1, max_values=1, options=options)

class TicketCategory(discord.ui.Select):
    def __init__(self, bot):
        with open('Configurations/TicketModule.json', encoding='utf-8-sig') as f:
            data = json.load(f)
        options = []
        for category, details in data['TICKET_CATEGORIES'].items():
            emoji = discord.utils.get(bot.emojis, name=details['Emoji']) # The emoji gets imported from the json file which is sent in the option
            options.append(SelectOption(label=category, value=category, emoji=emoji))
        super().__init__(placeholder="Select a ticket category...", min_values=1, max_values=1, options=options)