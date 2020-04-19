from classes import location, character
from npcs import shady_dock_worker
from characters import character_list
from objects import crate

name = "Dock"
description = "The dingy, seedy dock of the Renault. A place to make your fortune! Or get yourself killed."
adjoins = []
objects = [crate]
npcs = [shady_dock_worker]
grid = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', crate.crate, ' ', ' ', ' ', ' ', 'D'],
        ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', ' ', shady_dock_worker.shady_dock_worker, ' ', shady_dock_worker.shady_dock_worker, 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X']
]
character = character_list.anaxio
dock = location.Location(name, adjoins, description, npcs, objects, grid, character, 1, 1)

def main():
    dock.enter_room()
    dock.room_map()
    exited = False
    while not exited:
        user_command = input('').lower()
        if user_command == 'exit':
            exited = True
        # movement commands
        elif user_command == 'w':
            dock.move_character('west')
        elif user_command == "e":
            dock.move_character('east')
        elif user_command == 'n':
            dock.move_character('north')
        elif user_command == 's':
            dock.move_character('south')
        elif user_command == 'i':
            dock.trigger_interact()
        elif user_command == 'c':
            character.inventory_readout()
        else:
            print("Do you need a refresher on the controls?")
        dock.room_map()


main()
