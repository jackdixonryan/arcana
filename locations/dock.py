from classes import location
from npcs import shady_dock_worker

name = "Dock"
description = "The dingy, seedy dock of the Renault. A place to make your fortune! Or get yourself killed."
adjoins = []
objects = []
npcs = [shady_dock_worker]
grid = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', 'D'],
        ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X']
]
character = "sven"

dock = location.Location(name, adjoins, description, npcs, objects, grid, character, 1, 1)

def main():
    dock.enter_room()
    exited = False
    while not exited:
        direction = input('type n, s, e, w to move through the space.').lower()

        if direction == 'w':
            dock.move_character('west')
        elif direction == "e":
            dock.move_character('east')
        elif direction == 'n':
            dock.move_character('north')
        elif direction == 's':
            dock.move_character('south')
        else:
            print("please specify an actual direction.")
            exited = True


main()
