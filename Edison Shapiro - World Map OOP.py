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
tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')
tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')
tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')
tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')
tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')
tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')
tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')
tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')
tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')
tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')
tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')
tower = Room("Tower", None, 'rocks', None, 'shore', 'Defense Building')

current_node = tower
directions = ['north', 'south','east', 'west']

while True:
    print(current_node['NAME'])   # change
    print(current_node['DESCRIPTION'])   # Change
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
                # Change
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")