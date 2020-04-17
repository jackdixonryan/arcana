import random


class NPC:
    def __init__(self,
                 name: str,
                 description: str,
                 species: str,
                 inventory: list,
                 attack: float,
                 defense: float,
                 attitude: int,
                 interaction: dict):
        self.name = name
        self.description = description
        self.species = species
        self.inventory = inventory
        self.attack = attack
        self.defense = defense
        self.interaction = interaction
        self.attitude = attitude

    def interact(self, option):
        selected_interaction = self.interaction[option]
        if not selected_interaction:
            print("That\'s not really an option...")
        else:
            selected_interaction.get_response(self.attitude)
            for effect in selected_interaction.effects:
                for affected_attribute, change in effect.items():
                    current_value = getattr(self, affected_attribute)
                    new_value = current_value + change
                    setattr(self, affected_attribute, new_value)
        print("attitude:", self.attitude)

    def check_inventory(self):
        print("You look ", self.name, "over...")
        for inventory_item in self.inventory:
            print(inventory_item.name)

