import requests
import json

def fetch_all_cards():
    url = 'https://api.scryfall.com/bulk-data/default_cards'
    response = requests.get(url)
    data = response.json()
    
    download_uri = data['download_uri']
    response = requests.get(download_uri)
    cards = response.json()
    
    return cards

def organize_by_language(cards):
    card_database = {}
    for card in cards:
        lang = card['lang']
        if lang not in card_database:
            card_database[lang] = []
        card_database[lang].append(card['name'])
    
    return card_database

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    cards = fetch_all_cards()
    card_database = organize_by_language(cards)
    save_to_json(card_database, 'json/card_database.json')

if __name__ == "__main__":
    main()
