import random
import speech_recognition as sr

class BaseAI:
    def __init__(self, deck):
        self.deck = deck
        self.hand = []
        self.battlefield = []
        self.graveyard = []
        self.life_total = 40
        self.draw_initial_hand()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def draw_initial_hand(self):
        self.hand = random.sample(self.deck, 7)

    def draw_card(self):
        remaining_deck = list(set(self.deck) - set(self.hand))
        if remaining_deck:
            drawn_card = random.choice(remaining_deck)
            self.hand.append(drawn_card)
            print(f"AI draws {drawn_card}")

    def play_land(self):
        land_in_hand = [card for card in self.hand if "Land" in card]
        if land_in_hand:
            land_to_play = random.choice(land_in_hand)
            self.hand.remove(land_to_play)
            self.battlefield.append(land_to_play)
            print(f"AI plays land: {land_to_play}")

    def cast_spell(self):
        spells_in_hand = [card for card in self.hand if "Spell" in card]
        if spells_in_hand:
            spell_to_cast = random.choice(spells_in_hand)
            self.hand.remove(spell_to_cast)
            self.graveyard.append(spell_to_cast)
            print(f"AI casts spell: {spell_to_cast}")

    def respond_to_voice(self):
        print("Listening for your spell...")
        with self.microphone as source:
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio)
            print(f"You said: {command}")
            self.handle_command(command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")

    def handle_command(self, command):
        if "cast" in command.lower():
            spell_name = command.lower().replace("cast", "").strip()
            self.respond_to_spell(spell_name)

    def respond_to_spell(self, spell_name):
        print(f"AI responds to your spell: {spell_name}")
        # AI logic to respond to the spell goes here

    def take_turn(self):
        self.draw_card()
        self.play_land()
        self.cast_spell()
