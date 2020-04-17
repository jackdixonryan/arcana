from classes import item

name = "Crew Pants"
description = "Pants belonging to a former crew member, now deceased"
item_type = "Clothing"
weapon = False
wearable = True
has_buff = False
damage = None
protection = 10
buff = None
slot = "legs"
crew_pants = item.Item(name, description, item_type, weapon, wearable, has_buff, damage, protection, buff, slot)
