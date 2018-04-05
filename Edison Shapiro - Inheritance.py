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


class Sniper(Gun):
    def __init__(self, name, attack, description, ammo, long_range):
        super(Sniper, self).__init__(name, attack, description, ammo)
        self.long_range = long_range


class Armor(Item):
    def __init__(self, name, description, defense):
        super(Armor, self).__init__(name, description)
        self.defense = defense


class Helmet(Armor):
    def __init__(self, name, description, defense, skull_protection):
        super(Helmet, self).__init__(name, description, defense)
        self.skull_protection = skull_protection


class ChestPlate(Armor):
    def __init__(self, name, description, defense, chest_protection):
        super(ChestPlate, self).__init__(name, description, defense)
        self.chest_protection = chest_protection


class Leggings(Armor):
    def __init__(self, name, description, defense, leg_protection):
        super(Leggings, self).__init__(name, description, defense)
        self.leg_protection = leg_protection


class Gauntlets(Armor):
    def __init__(self, name, description, defense, arm_protection):
        super(Gauntlets, self).__init__(name, description, defense)
        self.arm_protection = arm_protection


class Boots(Armor):
    def __init__(self, name, description, defense, foot_protection):
        super(Boots, self).__init__(name, description, defense)
        self.foot_protection = foot_protection


class Consumable(Item):
    def __init__(self, name, description, use_option):
        super(Consumable, self).__init__(name, description)
        self.use_option = use_option


class BrightDust(Consumable):
    def __init__(self, name, description, use_option, uncommon_category):
        super(BrightDust, self).__init__(name, description, use_option)
        self.uncommon_category = uncommon_category


class BrightEngram(Consumable):
    def __init__(self, name, description, use_option, uncommon_engram):
        super(BrightEngram, self).__init__(name, description, use_option)
        self.uncommon_engram = uncommon_engram


class LegendaryShard(Consumable):
    def __init__(self, name, description, use_option, rare_category):
        super(LegendaryShard, self).__init__(name, description, use_option)
        self.rare_category = rare_category


class LuminousEngram(Consumable):
    def __init__(self, name, description, use_option, rare_engram):
        super(LuminousEngram, self).__init__(name, description, use_option)
        self.rare_engram = rare_engram