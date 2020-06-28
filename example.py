import json
with open('Neutral.json', 'r') as f:
    cardpool = json.load(f)
    card = cardpool["Robogoblin"]
    for key in card:
        print(f'{key:<12} -> {card[key]}')
