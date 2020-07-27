import json
import os
with open(f'{os.getcwd()}/en/all.json', 'r') as f:
        cardpool = json.load(f)

print('\nFate\'s Hand\n'
      f'{"id_":<10}{"related_":<23}{"expansion_"}')
for fh in [cardpool[c] for c in cardpool if cardpool[c]["name_"] == "Fate's Hand"]:
    print(f'{fh["id_"]} {fh["related_"]} {fh["expansion_"]}')

for k, v in cardpool['114031010'].items():
    print(f'{k:<13} -> ({str(type(v))[8:-2]}) {v}')
