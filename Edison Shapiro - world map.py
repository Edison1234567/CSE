world_map = {
    'TOWER': {
        'NAME': 'Tower',
        'DESCRIPTION': 'Defense Building',
        'PATHS': {
            'WEST': 'SHORE',
            'EAST': 'ROCKS'
        }
    },
    'SHORE': {
        'NAME': 'Shore',
        'DESCRIPTION': "Coast",
        'PATHS': {
            'SOUTH': 'CASTLE',
            'EAST': "TOWER"
        }
    },
    'CASTLE': {
        'NAME': 'Castle',
        'DESCRIPTION': "Medieval Building ",
        'PATHS': {
            'SOUTH': 'DUNGEON',
            'NORTH': "PASSAGE",
            'EAST': "Point B"
            'NORTH' 'SHORE'
        }
    },
    'DUNGEON': {
        'NAME': 'Dungeon',
        'DESCRIPTION': "Underground Cell",
        'PATHS': {
            'NORTH': 'Point B'
            'NORTH' 'CASTLE'
        }
    },
    'POINT B': {
        'NAME': 'Point B',
        'DESCRIPTION': 'Flag',
        'PATHS': {
            'NORTH': 'FALLS',
            'WEST': 'CASTLE'
        }
    },
    'FALLS': {
        'NAME': 'Falls',
        'DESCRIPTION': 'Waterfall',
        'PATHS': {
            'EAST': 'GROTTO'
            'SOUTH' 'POINT B'
        }
    },
    'GROTTO': {
        'NAME': 'GROTTO',
        'DESCRIPTION': 'Small Cave',
        'PATHS': {
            'NORTH': 'CAVE',
            'EAST': 'POINT C',
            'WEST': 'FALLS'
        }
    },
    'POINT C': {
        'NAME': 'Point C',
        'DESCRIPTION': 'Flag',
        'PATHS': {
            'NORTH': 'CAVE'
            'WEST' 'GROTTO'
        }
    },
    'CAVE': {
        'NAME': 'Cave',
        'DESCRIPTION': 'Dark Pathway',
        'PATHS': {
            'NORTH': 'MEADOW',
            'WEST': 'CRASH'
            'SOUTH' 'GROTTO'
            'SOUTH' 'POINT C'
        }
    },
    'MEADOW': {
        'NAME': 'Meadow',
        'DESCRIPTION': 'Grassland',
        'PATHS': {
            'WEST': 'CRASH'
            'SOUTH' 'CAVE'
        }
    },
    'CRASH': {
        'NAME': 'Crash',
        'DESCRIPTION': 'Ship Crash',
        'PATHS': {
            'WEST': 'KETCH',
            'EAST': 'MEADOW'
            'SOUTH' 'CAVE'
        }
    },
    'KETCH': {
        'NAME': 'Ketch',
        'DESCRIPTION': 'Ship',
        'PATHS': {
            'NORTH': 'POINT A',
            'SOUTH': 'ROCKS'
            'EAST' 'CRASH'
        }
    },
    'POINT A': {
        'NAME': 'Point A',
        'DESCRIPTION': 'Flag',
        'PATHS': {
            'SOUTH': 'KETCH'
        }
    },
    'ROCKS': {
        'NAME': 'Rocks',
        'DESCRIPTION': 'Stones',
        'PATHS': {
            'SOUTH': 'PASSAGE',
            'WEST': 'TOWER'
            'NORTH' 'KETCH'
        }
    },
    'PASSAGE': {
        'NAME': 'Passage',
        'DESCRIPTION': 'Through Way',
        'PATHS': {
            'SOUTH': 'CASTLE',
            'NORTH': 'ROCKS'
        }
    },
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
