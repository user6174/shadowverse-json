import json
import os
with open(f'{os.getcwd()}/Neutral.json', 'r') as f:
        cardpool = json.load(f)

card = cardpool["Robogoblin"]
for key in card:
    type_ = str(type(card[key]))[8:-2]
    print(f'{key:<13} -> ({type_}) {card[key]}')
