# Clash Royale API

A synchronous wrapper for the Official [Clash Royale API](https://developer.clashroyale.com).

## Installation
```sh
pip install git+https://github.com/mqfz/clashroyale
```

## Usage
```python
from clashroyale import ClashRoyale

cr = ClashRoyale(YOUR_TOKEN_HERE)

battles = cr.get_battle_log("#G9YV9GR8R")
latest_battle = battles[0]
supporting_cards = latest_battle.team[0].supporting_cards
assert isinstance(supporting_cards, list)
tower_troop = supporting_cards[0]

print(tower_troop.name)  # Tower Princess
```
