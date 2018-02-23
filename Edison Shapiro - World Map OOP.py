class Room(object):
    def __init__(self, name, north):
        self.name = name
        self.north = north

        def move(self, direction):
            global current_node
            current_node = globals()[getattr(self, direction)]


hdum = Room()

current_node = hdum
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