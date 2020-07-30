import json
import os
with open(f'{os.getcwd()}/en/all.json', 'r') as f:
        cardpool = json.load(f)

for k, v in cardpool['114031010'].items():
    print(f'{k:<13} -> ({str(type(v))[8:-2]}) {v}')
