
class Location:
    def __init__(self,
                 name: str,
                 adjoins: list,
                 description: str,
                 npcs: list,
                 objects: list
                 ):
        self.name = name
        self.adjoins = adjoins
        self.description = description
        self.npcs = npcs
        self.objects = objects
