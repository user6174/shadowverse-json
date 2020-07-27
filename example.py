import json
import os
with open(f'{os.getcwd()}/en/all.json', 'r') as f:
        cardpool = json.load(f)

card = cardpool['114031010']
for k, v in card.items():
    print(f'{k:<13} -> ({str(type(v))[8:-2]}) {v}')
