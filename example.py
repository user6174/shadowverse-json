import json
import os
# load the entire card library
cardpool = {}
for subdir, _, files in os.walk(os.getcwd()):
    for f in files:
        if str(f).endswith(".json"):
            with open(os.path.join(subdir, f), 'r') as jsonf:
                tmp = json.load(jsonf)
                for card in tmp:
                    cardpool[card] = tmp[card]
# usage example
card = cardpool["Robogoblin"]
for key in card:
    print(f'{key:<12} -> {card[key]}')
