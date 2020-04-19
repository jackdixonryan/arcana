from typing import Optional
from classes import item, character, npc, object


class Location:
    def __init__(self,
                 name: str,
                 adjoins: list,
                 description: str,
                 npcs: list,
                 objects: list,
                 grid: list,
                 current_character: Optional = None,
                 character_x_position: Optional[int] = None,
                 character_y_position: Optional[int] = None,
                 door_positions: Optional[list] = None
                 ):
        self.name = name
        self.adjoins = adjoins
        self.description = description
        self.npcs = npcs
        self.objects = objects
        self.grid = grid
        self.current_character = current_character
        self.character_x_position = character_x_position
        self.character_y_position = character_y_position
        self.door_positions = door_positions

    def room_map(self):
        display_map = []
        for row in self.grid:
            display_row = []
            for position in row:
                # this will tell us what we have
                if position == "X":
                    display_row.append("■")
                elif position == "Y":
                    display_row.append("▵")
                elif position == "D":
                    display_row.append("▢")
                elif isinstance(position, npc.NPC):
                    display_row.append("Ω")
                elif isinstance(position, object.Object):
                    display_row.append(position.symbol)
                else:
                    display_row.append(" ")
            display_map.append(display_row)
            separator = "  "
            print(separator.join(display_row))

    # needs refactor
    def enter_room(self):
        self.grid[self.character_y_position][self.character_x_position] = "Y"
        self.room_map()

    def move_character(self, direction):
        old_character_x_position = self.character_x_position
        old_character_y_position = self.character_y_position
        if direction == 'east':
            new_character_x_position = old_character_x_position + 1
            desired_new_position = self.grid[old_character_y_position][new_character_x_position]
            if desired_new_position == " ":
                self.grid[old_character_y_position][new_character_x_position] = "Y"
                self.grid[old_character_y_position][old_character_x_position] = " "
                self.character_x_position = new_character_x_position
        elif direction == 'west':
            new_character_x_position = old_character_x_position - 1
            desired_new_position = self.grid[old_character_y_position][new_character_x_position]
            if desired_new_position == " ":
                self.grid[old_character_y_position][new_character_x_position] = "Y"
                self.grid[old_character_y_position][old_character_x_position] = " "
                self.character_x_position = new_character_x_position
        elif direction == 'north':
            new_character_y_position = old_character_y_position - 1
            desired_new_position = self.grid[new_character_y_position][old_character_x_position]
            if desired_new_position == " ":
                self.grid[new_character_y_position][old_character_x_position] = "Y"
                self.grid[old_character_y_position][old_character_x_position] = " "
                self.character_y_position = new_character_y_position
        elif direction == 'south':
            new_character_y_position = old_character_y_position + 1
            desired_new_position = self.grid[new_character_y_position][old_character_x_position]
            if desired_new_position == " ":
                self.grid[new_character_y_position][old_character_x_position] = "Y"
                self.grid[old_character_y_position][old_character_x_position] = " "
                self.character_y_position = new_character_y_position

    def trigger_interact(self):
        possible_targets = [
            self.grid[self.character_y_position - 1][self.character_x_position],
            self.grid[self.character_y_position + 1][self.character_x_position],
            self.grid[self.character_y_position][self.character_x_position - 1],
            self.grid[self.character_y_position][self.character_x_position + 1]
        ]
        eligible_targets = []
        for possible_target in possible_targets:
            if isinstance(possible_target, npc.NPC) or isinstance(possible_target, object.Object):
                eligible_targets.append(possible_target)
        # now we check to see if there are more than one targets the user might be electing to use.
        if len(eligible_targets) > 1:
            options = ['a', 'b', 'c', 'd']
            choices = []
            i = 0
            for eligible_target in eligible_targets:
                choices.append(options[i] + ": " + eligible_target.name)
                i += 1
            joiner = "\n"
            choice_readout = joiner.join(choices)
            print("Choose an Option")
            selection = input(choice_readout)
            if selection in options:
                print(i)
        # if there is only one option
        elif len(eligible_targets) == 1:
            target = eligible_targets[0]
            if isinstance(target, npc.NPC):
                interactions = target.list_interactions()
                str_prompt = "Type an option: " + ", ".join(interactions) + ": "
                choice_of_interaction = input(str_prompt)
                if choice_of_interaction in interactions:
                    target.interact(choice_of_interaction)
                else:
                    print('That is not a valid option.')
            elif isinstance(target, object.Object):
                handle_object_interaction(target, self.current_character)

    def enter_character(self, new_character, character_x_position, character_y_position):
        self.current_character = new_character
        self.character_x_position = character_x_position
        self.character_y_position = character_y_position

def handle_object_interaction(object, character):
    # if the object cannot be interacted with, simply trigger inspection.
    if object.inert_object:
        object.inspect_object()
    else:
        actions = object.actions
        print('What do you want to do?')
        for action in actions.values():
            print(action.name)
        desired_action = input(' ')
        coded = '_'.join(desired_action.split(' ')).lower()
        if coded in actions.keys():
            object.actions[coded].use(character)
        else:
            print('That is not a valid choice.')

