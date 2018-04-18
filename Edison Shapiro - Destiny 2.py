class Character(object):
    def __init__(self, name, attack, gun, sword, armor):
        self.name = name
        self.health = 120
        self.attack = attack
        self.gun = gun
        self.sword = sword
        self.armor = armor
        self.inventory = []

    def take_damage(self, amt):
        self.health -= amt

    def attack(self):
        player.take_damage(self.attack)

    def death(self):
        if self.health == 0:
            print("You Died")

    def use_armor(self, armor):
        self.armor = armor


player = Character("Test", 0, 0, 0, 0)
player.use_armor(2)


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
cave = Room("Cave", 'Meadow', 'point_c', 'grotto', 'crash', 'Dark Pathway')
meadow = Room("Meadow", None, None, 'cave', 'crash', 'Grassland')
crash = Room("crash", None, 'meadow', 'cave', 'ketch', 'Ship Crash')
ketch = Room("Ketch", 'point_a', 'crash', 'rocks', None, 'Ship')
point_a = Room("Point_a", None, None, 'ketch', None, 'Flag')
rocks = Room("rocks", 'ketch', None, 'passage', 'tower', 'Stones')
passage = Room("passage", 'rocks', None, 'castle', None, 'Through Way')

current_node = tower
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self):
        print("You use the %s" % self.name)


class Vehicle(Item):
    def __init__(self, name, description, transport):
        super(Vehicle, self).__init__(name, description)
        self.transport = transport

    def summon(self):
        print("You summon the vehicle")


class Ship(Vehicle):
    def __init__(self, name, description, transport, space_travel):
        super(Ship, self).__init__(name, description, transport)
        self.space_travel = space_travel

    def transport(self):
        print("You transport your ship using %s" % self.space_travel)


class Sparrow(Vehicle):
    def __init__(self, name, description, transport, land_travel):
        super(Sparrow, self).__init__(name, description, transport)
        self.land_travel = land_travel

    def transport(self):
        print("You transport your sparrow using %s" % self.land_travel)


class Weapon(Item):
    def __init__(self, name, attack, description):
        super(Weapon, self).__init__(name, description)
        self.attack = attack

    def attack(self):
        print("You attack with the %s" % self.attack)


class Sword(Weapon):
    def __init__(self, name, sharp_blade, attack, description):
        super(Sword, self).__init__(name, attack, description)
        self.sharp_blade = sharp_blade

    def swing(self):
        print("You swing the sword and the %s kills a fallen" % self.sharp_blade)


class Gun(Weapon):
    def __init__(self, name, attack, description, ammo):
        super(Gun, self).__init__(name, attack, description)
        self.ammo = ammo

    def reload(self):
        print("You reload your gun with %s" % self.ammo)


class PulseRifle(Gun):
    def __init__(self, name, attack, description, ammo, five_round):
        super(PulseRifle, self).__init__(name, attack, description, ammo)
        self.five_round = five_round

    def shoot(self):
        print("You use %s and shoot 5 shots" % self.five_round)


class ScoutRifle(Gun):
    def __init__(self, name, attack, description, ammo, precision):
        super(ScoutRifle, self).__init__(name, attack, description, ammo)
        self.precision = precision

    def shoot(self):
        print("You shoot the ScoutRifle and you get a %s shot on the fallen" % self.precision)


class Sidearm(Gun):
    def __init__(self, name, attack, description, ammo, high_rate_of_fire):
        super(Sidearm, self).__init__(name, attack, description, ammo)
        self.high_rate_of_fire = high_rate_of_fire

    def shoot(self):
        print("You shoot the Sidearm and the %s kills a fallen" % self.high_rate_of_fire)


class HandCannon(Gun):
    def __init__(self, name, attack, description, ammo, calm_hand):
        super(HandCannon, self).__init__(name, attack, description, ammo)
        self.calm_hand = calm_hand

    def shoot(self):
        print("The %s helps you aim in close-quarters firing as you shoot your gun and kill fallen" % self.calm_hand)


class AutoRifle(Gun):
    def __init__(self, name, attack, description, ammo, all_round):
        super(AutoRifle, self).__init__(name, attack, description, ammo)
        self.all_round = all_round

    def shoot(self):
        print("You shoot the AutoRifle and the gun fires the %s" % self.all_round)


class Sniper(Gun):
    def __init__(self, name, attack, description, ammo, long_range):
        super(Sniper, self).__init__(name, attack, description, ammo)
        self.long_range = long_range

    def shoot(self):
        print("You shoot the Sniper gun and the %s precision head shots a fallen" % self.long_range)


class Armor(Item):
    def __init__(self, name, description, defense):
        super(Armor, self).__init__(name, description)
        self.defense = defense

    def protect(self):
        print("The Armor gives %s to the user" % self.defense)


class Helmet(Armor):
    def __init__(self, name, description, defense, skull_protection):
        super(Helmet, self).__init__(name, description, defense)
        self.skull_protection = skull_protection

    def skull_protection(self):
        print("The Helmet gives you %s" % self.skull_protection)


class ChestPlate(Armor):
    def __init__(self, name, description, defense, chest_protection):
        super(ChestPlate, self).__init__(name, description, defense)
        self.chest_protection = chest_protection

    def chest_protection(self):
        print("The ChestPlate gives you %s" % self.chest_protection)


class Leggings(Armor):
    def __init__(self, name, description, defense, leg_protection):
        super(Leggings, self).__init__(name, description, defense)
        self.leg_protection = leg_protection

    def leg_protection(self):
        print("The Leggings give you %s" % self.leg_protection)


class Gauntlets(Armor):
    def __init__(self, name, description, defense, arm_protection):
        super(Gauntlets, self).__init__(name, description, defense)
        self.arm_protection = arm_protection

    def arm_protection(self):
        print("The Gauntlets give you %s" % self.arm_protection)


class Boots(Armor):
    def __init__(self, name, description, defense, foot_protection):
        super(Boots, self).__init__(name, description, defense)
        self.foot_protection = foot_protection

    def foot_protection(self):
        print("The Boots give you %s" % self.foot_protection)


class Consumable(Item):
    def __init__(self, name, description, use_option):
        super(Consumable, self).__init__(name, description)
        self.use_option = use_option

    def use(self):
        print("You use the %s" % self.use_option)


class BrightDust(Consumable):
    def __init__(self, name, description, use_option, uncommon_category):
        super(BrightDust, self).__init__(name, description, use_option)
        self.uncommon_category = uncommon_category

    def combine(self):
        print("If there is multiple of this item in the %s combine to make BrightEngram" % self.uncommon_category)


class BrightEngram(Consumable):
    def __init__(self, name, description, use_option, uncommon_engram):
        super(BrightEngram, self).__init__(name, description, use_option)
        self.uncommon_engram = uncommon_engram

    def open(self):
        print("Opens BrightEngram and the item is a armor piece or a weapon in the %s category" % self.uncommon_engram)


class LegendaryShard(Consumable):
    def __init__(self, name, description, use_option, rare_category):
        super(LegendaryShard, self).__init__(name, description, use_option)
        self.rare_category = rare_category

    def combine(self):
        print("If there is a multiple of this item in the %s combine to make a LuminousEngram" % self.rare_category)


class LuminousEngram(Consumable):
    def __init__(self, name, description, use_option, rare_engram):
        super(LuminousEngram, self).__init__(name, description, use_option)
        self.rare_engram = rare_engram

    def open(self):
        print("Opens LuminousEngram and the item is a armor piece or a weapon in the %s category" % self.rare_engram)


while True:
    # Room Information
    print(current_node.name)
    print(current_node.description)

    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)

    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    # How to handle commands
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")

    elif command[:7] == "pick up":
        item = command[8:]
        print("You have picked up the %s" % item)
    elif command[:4] == "kill":
        vandal = command[:6]
        print("You have killed the fallen vandal")
    
    else:
        print("Command not recognized")
        



