
from classes import location, character
from objects import object_list
barstool = object_list.stool
counter = object_list.counter
booth = object_list.booth
table = object_list.table
hologram = object_list.hologram

name = "Anaxio's Bar"
description = "It was the station's center! Once upon a time, at least..."
adjoins = []
npcs = []
objects = []
grid = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', booth, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', table, ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', 'X'],
        ['X', booth, ' ', counter, counter, counter, counter, counter, counter, counter, counter, counter, 'X'],
        ['X', ' ', ' ', ' ', barstool, ' ', barstool, ' ', barstool, ' ', barstool, ' ', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', booth, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', table, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', booth, booth, table, booth, table, booth, ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', hologram, ' ', ' ', ' ', ' ', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' ', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'D', 'X', 'X', 'X'],
]

anaxios_bar = location.Location(name, adjoins, description, npcs, objects, grid, character, 1, 1)
