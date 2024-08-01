import json
import requests

class AIOpponent:
    def __init__(self, name, decklist_url):
        self.name = name
        self.decklist = self.fetch_decklist(decklist_url)

    def fetch_decklist(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

def create_ai_opponent(name, decklist_url):
    return AIOpponent(name, decklist_url)
