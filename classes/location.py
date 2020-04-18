from typing import Optional


class Location:
    def __init__(self,
                 name: str,
                 adjoins: list,
                 description: str,
                 npcs: list,
                 objects: list,
                 grid: list,
                 character,
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
        self.character = character
        self.character_x_position = character_x_position
        self.character_y_position = character_y_position
        self.door_positions = door_positions

    def room_map(self):
        for row in self.grid:
            row = [char.replace('Y', '◬') for char in row]
            row = [char.replace('X', "▦") for char in row]
            row = [char.replace('D', "▯") for char in row]
            separator = "  "
            print(separator.join(row))

    def enter_room(self):
        self.grid[self.character_y_position][self.character_x_position] = "Y"
        self.room_map()

    def move_character(self, direction):
        old_character_x_position = self.character_x_position
        old_character_y_position = self.character_y_position
        if direction == 'east':
            new_character_x_position = old_character_x_position + 1
            desired_new_position = self.grid[old_character_y_position][new_character_x_position]
            if not desired_new_position == "X":
                self.grid[old_character_y_position][new_character_x_position] = "Y"
                self.grid[old_character_y_position][old_character_x_position] = " "
                self.character_x_position = new_character_x_position
        elif direction == 'west':
            new_character_x_position = old_character_x_position - 1
            desired_new_position = self.grid[old_character_y_position][new_character_x_position]
            if not desired_new_position == "X":
                self.grid[old_character_y_position][new_character_x_position] = "Y"
                self.grid[old_character_y_position][old_character_x_position] = " "
                self.character_x_position = new_character_x_position
        elif direction == 'north':
            new_character_y_position = old_character_y_position - 1
            desired_new_position = self.grid[new_character_y_position][old_character_x_position]
            if not desired_new_position == "X":
                self.grid[new_character_y_position][old_character_x_position] = "Y"
                self.grid[old_character_y_position][old_character_x_position] = " "
                self.character_y_position = new_character_y_position
        elif direction == 'south':
            new_character_y_position = old_character_y_position + 1
            desired_new_position = self.grid[new_character_y_position][old_character_x_position]
            if not desired_new_position == "X":
                self.grid[new_character_y_position][old_character_x_position] = "Y"
                self.grid[old_character_y_position][old_character_x_position] = " "
                self.character_y_position = new_character_y_position
        self.room_map()
