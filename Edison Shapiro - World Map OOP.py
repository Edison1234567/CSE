class Room(object):
    def __init__(self, name, north, east, south, west, description):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.description = description

    def move(self, direction):
                global current_node
                current_node = globals()[getattr(self, direction)]


tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')
shore = Room("Shore", None, 'tower', 'castle', None, 'Coast')
castle = Room("Castle", 'passage, shore', 'point b', 'dungeon', None, 'Medieval Building')
dungeon = Room("Dungeon", 'point_b, castle', None, None, None, 'Underground Cell')
point_b = Room("Point_B", 'falls', None, None, 'castle', 'Flag')
falls = Room("Falls", None, 'grotto', 'point_b', None, 'Waterfall')
grotto = Room("Grotto", 'cave', 'point_c', None, 'falls', 'Small Cave')
point_c = Room("Point_c", 'cave', None, None, 'grotto', 'Flag')
cave = Room("Cave", 'Meadow', 'point_c', 'grotto', 'crash','Dark Pathway')
meadow = Room("Meadow", None, None, 'cave', 'crash', 'Grassland')
crash = Room("crash", None, 'meadow', 'cave', 'ketch', 'Ship Crash')
ketch = Room("Ketch", 'point_a', 'crash', 'rocks', None, 'Ship')
point_a = Room("Point_a", None, None, 'ketch', None, 'Flag')
rocks = Room("rocks", 'ketch', None, 'passage', 'tower', 'Stones')
passage = Room("passage", 'rocks', None, 'castle', None, 'Through Way')

current_node = tower
directions = ['north', 'south','east', 'west']

while True:

        print(self.name)   # Change
        print(self.description)   # Change
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            #  Change
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")