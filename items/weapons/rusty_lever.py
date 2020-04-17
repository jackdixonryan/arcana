from classes import item

name = "Rusty Lever"
description = "I guess this could hurt somebody."
item_type = "Weapon"
weapon = True
wearable = False
has_buff = False
damage = 2.5
protection = None
buff = None
slot = "weapon"
rusty_lever = item.Item(name, description, item_type, weapon, wearable, has_buff, damage, protection, buff, slot)
