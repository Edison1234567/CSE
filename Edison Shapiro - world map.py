world_map = {
    'TOWER': {
        'NAME': 'Tower',
        'DESCRIPTION': '.',
        'PATHS': {
            'WEST': 'SHORE',
            'EAST': 'ROCKS'
        }
    },
    'SHORE': {
        'NAME': 'Shore',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'SOUTH': 'CASTLE',
            'EAST': "TOWER"
        }
    },
    'CASTLE': {
        'NAME': 'Castle',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'SOUTH': 'DUNGEON',
            'NORTH': "Passage"
        }
    },
    '': {
        'NAME': 'East of House',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    }
}

current_node = world_map['TOWER']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
