from classes import location
from npcs import shady_dock_worker

name = "Dock"
description = "The dingy, seedy dock of the Renault. A place to make your fortune! Or get yourself killed."
adjoins = []
objects = []
npcs = [shady_dock_worker]
grid = [[' ', ' ', ' ', ' ', ' ']]]

dock = location.Location(name, adjoins, description, npcs, objects)
