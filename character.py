import item

class Character:
    def __init__(self,
                 name: str,
                 skills: dict,
                 inventory: list,
                 worn_equipment: dict,
                 vitals: dict):
        self.name = name

        valid_skills = ["athletics",
                        "spacefaring",
                        "accuracy",
                        "gunslinger",
                        "planetary_survival",
                        "strength",
                        "linguistics"]

        for new_skill in skills.keys():
            if new_skill not in valid_skills:
                raise ValueError("Skill " + new_skill + " is not permitted by the current build.")

        self.skills = skills
        self.inventory = inventory
        self.worn_equipment = worn_equipment

        if vitals['health'] and vitals['strength'] and vitals['energy']:
            self.vitals = vitals
        else:
            raise ValueError("'Vitals must include 'health', 'strength', and 'energy''")

    def say_name(self):
        print("My name is ", self.name)

    def gain_xp(self, skill, xp_gain):
        current_xp = self.skills[skill]
        new_xp = current_xp + xp_gain
        self.skills[skill] = new_xp

    def show_skill_xp_quantities(self):
        for skill, xp in self.skills.items():
            print(skill, ":", xp, "XP")

    def show_vitals(self):
        for vital, status in self.vitals.items():
            print(vital, ":", str(status))

    def add_item_to_inventory(self, new_item):
        self.inventory.append(new_item)

    def inventory_readout(self):
        if len(self.inventory) > 0:
            for inventory_item in self.inventory:
                print(inventory_item.name)
        else:
            print("inventory is empty")

    def inspect_inventory_item(self, inventory_item_name):
        desired_item = next((inventory_item for inventory_item in self.inventory if inventory_item.name == inventory_item_name), None)
        print("_________________________")
        print(desired_item.name.upper())
        print("*===*===*===*===*===*===*")
        print("Description:", desired_item.description)
        print("Type:", desired_item.item_type)
        if desired_item.weapon:
            print("Damage:", desired_item.damage)
        if desired_item.wearable:
            print("Protection:", desired_item.protection)
        if desired_item.has_buff:
            for buff, effect in desired_item.buff.items():
                print(buff, ":", effect)
        print("_________________________")

    def equip_item(self, inventory_item_name):
        desired_item = next((inventory_item for inventory_item in self.inventory if inventory_item.name == inventory_item_name), None)
        if desired_item.weapon or desired_item.wearable:
            desired_slot = desired_item.slot
            currently_equipped = self.worn_equipment[desired_slot]
            # if nothing is equipped
            if not currently_equipped:
                self.worn_equipment[desired_slot] = desired_item
            # if there's already something equipped in that slot.
            else:
                self.inventory.append(currently_equipped)
                self.worn_equipment[desired_slot] = desired_item
            # finally, the item itself must be removed from the inventory
            self.inventory.remove(desired_item)
        else:
            print("That item cannot be equipped.")


character = Character('Anaxio',
                      {
                          'gunslinger': 0,
                          'athletics': 0,
                          'spacefaring': 0,
                          'accuracy': 0,
                          'planetary_survival': 0,
                          'strength': 0,
                          'linguistics': 0
                      },
                      [],
                      {
                          'body': None,
                          'head': None,
                          'hands': None,
                          'legs': None,
                          'feet': None
                      },
                      {'health': 100,
                       'strength': 100,
                       'energy': 100
                       })
# character.say_name()
# character.show_skill_xp_quantities()
# character.gain_xp('gunslinger', 20)
# character.show_skill_xp_quantities()
# character.show_vitals()

crew_shirt = item.Item('crew shirt',
                       'the shirt of a recently deceased crew member',
                       'clothing',
                       False,
                       True,
                       False,
                       None,
                       10,
                       None,
                       "body")

character.add_item_to_inventory(crew_shirt)
character.inventory_readout()
character.equip_item('crew shirt')
character.inventory_readout()

