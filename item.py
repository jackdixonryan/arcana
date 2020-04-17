from typing import Optional


class Item:
    def __init__(self,
                 name: str,
                 description: str,
                 item_type: str,
                 weapon: bool,
                 wearable: bool,
                 has_buff: bool,
                 damage: Optional[float] = None,
                 protection: Optional[float] = None,
                 buff: Optional[dict] = None,
                 slot: Optional[str] = None):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.weapon = weapon
        self.wearable = wearable
        self.has_buff = has_buff
        if damage:
            self.damage = damage
        if protection:
            self.protection = protection
        if buff:
            self.buff = buff
        if slot:
            self.slot = slot
