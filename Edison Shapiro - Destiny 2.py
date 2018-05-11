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


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self):
        print("You use the %s" % self.name)


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


class Shotgun(Gun):
    def __init__(self, name, attack, description, ammo, one_round):
        super(Shotgun, self).__init__(name, attack, description, ammo)
        self.one_round = one_round

    def shoot(self):
        print("the shotgun does incredible amount of damage if in close combat range with %s" % self.one_round)


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


sword = Sword('Sword', 'sharp_blade', 'attack', 'The sword has a long, sharp blade with a hilt to hold the sword with')
shotgun = Shotgun('Shotgun', 'attack', 'The Shotgun has great impact range and stability has one shot and'
                                       'does incredible amount of damage if in close combat', 'ammo', 'one_round')
pulseRifle = PulseRifle('PulseRifle', ' attack', 'The PulseRifle has a Long shooting rifle with a zoom in option'
                                                 ' while shooting, takes 5 shots at a time and has good stability',
                        'ammo', 'five_round')
scoutRifle = ScoutRifle('ScoutRifle', 'attack', 'The ScoutRifle has a medium size, it has a scope for long range,'
                                                ' and has good handling and reload speed', 'ammo', 'precision')
sidearm = Sidearm('Sidearm', 'attack', 'The Sidearm is a short gun, it has good rate of fire, stability, and reload, '
                                       'it also has good rate of fire', 'ammo', 'high_rate_of_fire')
handCannon = HandCannon('HandCannon', 'attack', 'The HandCannon is a medium sized gun, it has good impact,'
                                                ' and is good for close combat', 'ammo', 'calm_hand')
autoRifle = AutoRifle('AutoRifle', 'attack', 'The AutoRifle is a long gun, it has a scope, good range, good handling,'
                                             ' and shoots all rounds at once', 'ammo', 'all_round')
sniper = Sniper('Sniper', 'attack', 'The Sniper is a long gun, has a scope, cross map range, and has good impact',
                'ammo', 'long_range')
helmet = Helmet('Helmet', 'The helmet has good recovery and mobility, as well as giving skull protection', 'defense',
                'skull_protection')
chestPlate = ChestPlate('ChestPlate', 'The Chest Plate gives good resistance and mobility,'
                                      ' it also gives good chest protection', 'defense', 'chest_protection')
legging = Leggings('Leggings', 'The leggings give good recovery and mobility, it also gives good leg armor', 'defence',
                   'leg_protection')
gauntlet = Gauntlets('Gauntlets', 'The gauntlets give good mobility and recovery, it also gives good arm protection',
                     'defense', 'arm_protection')
boot = Boots('Boots', 'The boots give good mobility and recovery, it also give good foot protection', 'defense',
             'foot_protection')
brightDust = BrightDust('BrightDust', 'Combine 50 bright dust to make a bright engram', 'use_option',
                        'uncommon_category')
brightEngram = BrightEngram('BrightEngram', 'Use a bright engram to get a armor piece or '
                                            'a weapon of the uncommon category', 'use_option', 'uncommon_engram')
legendaryShard = LegendaryShard('LegendaryShard', 'Combine 100 legendary shards to make a luminous engram',
                                'use_option', 'rare_category')
luminousEngram = LuminousEngram('LuminousEngram', 'Use a Luminous Engram to get a armor piece or a weapon of the rare'
                                                  'category', 'use_option', 'rare_engram')


class Room(object):
    def __init__(self, name, north, east, south, west, description, items):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.description = description
        self.items = items

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


tower = Room("Tower", None, 'rocks', None, 'shore', 'Medieval Tower', sword)
shore = Room("Shore", None, 'tower', 'castle', None, 'Coast', shotgun)
castle = Room("Castle", 'passage, shore', 'point b', 'dungeon', None, 'Medieval Building', pulseRifle)
dungeon = Room("Dungeon", 'point_b, castle', None, None, None, 'Underground Cell', scoutRifle)
point_b = Room("Point_B", 'falls', None, None, 'castle', 'Flag', sidearm)
falls = Room("Falls", None, 'grotto', 'point_b', None, 'Waterfall', handCannon)
grotto = Room("Grotto", 'cave', 'point_c', None, 'falls', 'Small Cave', autoRifle)
point_c = Room("Point_c", 'cave', None, None, 'grotto', 'Flag', sniper)
cave = Room("Cave", 'Meadow', 'point_c', 'grotto', 'crash', 'Dark Pathway', helmet)
meadow = Room("Meadow", None, None, 'cave', 'crash', 'Grassland', chestPlate)
crash = Room("crash", None, 'meadow', 'cave', 'ketch', 'Ship Crash', legging)
ketch = Room("Ketch", 'point_a', 'crash', 'rocks', None, 'Ship', gauntlet)
point_a = Room("Point_a", None, None, 'ketch', None, 'Flag', boot)
rocks = Room("rocks", 'ketch', None, 'passage', 'tower', 'Stones', brightDust)
passage = Room("passage", 'rocks', None, 'castle', None, 'Through Way', legendaryShard)

current_node = tower
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

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
        item_requested = command[8:]
        if current_node.items is not None and item_requested.lower() == current_node.items.name.lower():
            print("You have picked up the %s" % item_requested)
            player.inventory.append(current_node.items)
            current_node.items = None
        else:
            print("I don't see it here")
    elif command[:9] == "inventory":
        for item in player.inventory:
            print(item.name)
    elif command[:5] == "equip":
        item_requested = command[6:]
        found = False
        for item in player.inventory:
            if item_requested.lower() == item.name.lower():
                print("You have selected the %s to equip" % item_requested)
                found = True
        if not found:
            print("I don't see that item in your inventory")
    elif command[:3] == "use":
        item_requested = command[4:]
        found = False
        for item in player.inventory:
            if item_requested.lower() == item.name.lower():
                found = True
                item.use()
                player.inventory.remove(item)
        if not found:
            print("I don't see that item in your inventory")
    elif command[:4] == "kill":
        vandal = command[6:]
        print("You have killed the fallen")
    
    else:
        print("Command not recognized")
    print()
        



