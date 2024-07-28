# ai_opponents/jiwon_ai.py

from opponent_base import OpponentBase

class JiwonAI(OpponentBase):
    def __init__(self):
        deck = [
            "Rin and Seri, Inseparable",
            "Ajani's Pridemate",
            "Ajani, the Greathearted",
            "Alpine Watchdog",
            "Animal Sanctuary",
            "Annie Joins Up",
            "Arcane Signet",
            "Blossoming Sands",
            "Bolt Hound",
            "Boros Signet",
            "Bronzehide Lion",
            "Cabaretti Charm",
            "Cabaretti Courtyard",
            "Camaraderie",
            "Canopy Vista",
            "Cinder Glade",
            "Collective Blessing",
            "Command Tower",
            "Commander's Sphere",
            "Crib Swap",
            "Cultivate",
            "Dictate of Heliod",
            "Evolving Wilds",
            "Exotic Orchard",
            "Faithful Watchdog",
            "Farseek",
            "Felidar Cub",
            "Felidar Retreat",
            "Feline Sovereign",
            "Fleecemane Lion",
            "Forest",
            "Forest",
            "Forest",
            "Forest",
            "Forest",
            "Forest",
            "Forest",
            "Gruul Signet",
            "Harmonize",
            "Hour of Reckoning",
            "Inspiring Leader",
            "Instruments of War",
            "Intangible Virtue",
            "Irregular Cohort",
            "Jazal Goldmane",
            "Jetmir, Nexus of Revels",
            "Jinnie Fay, Jetmir's Second",
            "Jungle Shrine",
            "Kaheera, the Orphanguard",
            "Keeper of Fables",
            "King of the Pride",
            "Kutzil, Malamet Exemplar",
            "Loyal Warhound",
            "Make a Stand",
            "Masked Vandal",
            "Mirror Entity",
            "Mountain",
            "Mountain",
            "Myriad Landscape",
            "Naya Charm",
            "Overrun",
            "Pack Leader",
            "Path of Ancestry",
            "Plains",
            "Plains",
            "Plains",
            "Plains",
            "Plains",
            "Plains",
            "Plains",
            "Plains",
            "Plains",
            "Plains",
            "Plains",
            "Prava of the Steel Legion",
            "Pridemalkin",
            "Qasali Pridemage",
            "Rambunctious Mutt",
            "Rampant Growth",
            "Regal Caracal",
            "Release the Dogs",
            "Resolute Watchdog",
            "Rootborn Defenses",
            "Roxanne, Starfall Savant",
            "Rugged Highlands",
            "Sacred Cat",
            "Selfless Savior",
            "Shamanic Revelation",
            "Sol Ring",
            "Spirited Companion",
            "Swords to Plowshares",
            "Taurean Mauler",
            "Terramorphic Expanse",
            "Tesak, Judith's Hellhound",
            "Trusty Retriever",
            "Unbreakable Formation",
            "Universal Automaton",
            "White Sun's Zenith",
            "Whitemane Lion",
            "Wind-Scarred Crag"
        ]
        super().__init__("Jiwon", deck, difficulty=5)

    def play_turn(self):
        # Basic AI logic to play cards from hand
        for card in self.hand:
            if self.can_play_card(card):
                self.battlefield.append(card)
                self.hand.remove(card)
                print(f"{self.name} played {card}")
                break  # Play one card per turn for simplicity

    def can_play_card(self, card):
        # Simplified logic to decide if a card can be played
        return True  # Placeholder logic

    def respond_to_spell(self, spell):
        # Simplified logic to respond to a spell
        print(f"{self.name} has no response to {spell}")
