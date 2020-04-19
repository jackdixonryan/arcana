import layout.generate_base_text_display
from typing import Optional


class Object:
    def __init__(self,
                 name: str,
                 description: str,
                 actions: dict,
                 container: bool,
                 skill_object: bool,
                 inert_object: bool,
                 symbol: str,
                 contents: Optional[list] = None,
                 ):
        self.name = name
        self.description = description
        self.actions = actions
        self.container = container
        self.skill_object = skill_object
        self.inert_object = inert_object
        self.contents = contents
        self.symbol = symbol

    def inspect_object(self):
        readout = layout.generate_base_text_display.generate_dialog_box(self.name, self.description)
        print(readout)

    def use_object(self, usage, character):
        desired_objective = self.actions[usage]
        desired_objective.use(character)



# from characters import character_list
# from classes import action
#
# anaxio = character_list.anaxio
#
# chat_up = action.create_action("Chat Up", "skilling", "linguistics", 2.5)
# hologram = Object("Hologram", "It wants to talk", { 'chat_up': chat_up }, False, True, False, None)
#
# hologram.use_object('chat_up', anaxio)
# anaxio.show_skill_xp_quantities()
