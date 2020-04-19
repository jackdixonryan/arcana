from classes import character

name = "Anaxio Balfour"
skills = {"athletics": 0,
          "spacefaring": 0,
          "accuracy": 0,
          "gunslinger": 0,
          "planetary_survival": 0,
          "strength": 0,
          "linguistics": 0}
inventory = []
worn_equipment = {}
vitals = {
    "health": 100,
    "energy": 100,
    'strength': 100
}
anaxio = character.create(name, skills, inventory, worn_equipment, vitals)
