class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, name, attack, description):
        super(Weapon, self).__init__(name, description)
        self.attack = attack


class Sword(Weapon):
    def __init__(self, name, sharp_blade, attack, description):
        super(Sword, self).__init__(name, attack, description)
        self.sharp_blade = sharp_blade


class Gun(Weapon):
    def __init__(self, name, attack, description, ammo):
        super(Gun, self).__init__(name, attack, description)
        self.ammo = ammo


class PulseRifle(Gun):
    def __init__(self, name, attack, description, ammo, five_round):
        super(PulseRifle, self).__init__(name, attack, description, ammo)
        self.five_round = five_round


class ScoutRifle(Gun):
    def __init__(self, name, attack, description, ammo, precision):
        super(ScoutRifle, self).__init__(name, attack, description, ammo)
        self.precision = precision


class Sidearm(Gun):
    def __init__(self, name, attack, description, ammo, high_rate_of_fire):
        super(Sidearm, self).__init__(name, attack, description, ammo)
        self.high_rate_of_fire = high_rate_of_fire


class HandCannon(Gun):
    def __init__(self, name, attack, description, ammo, calm_hand):
        super(HandCannon, self).__init__(name, attack, description, ammo)
        self.calm_hand = calm_hand


class AutoRifle(Gun):
    def __init__(self, name, attack, description, ammo, all_round):
        super(AutoRifle, self).__init__(name, attack, description, ammo)
        self.all_round = all_round


class Sniper(Gun):
    def __init__(self, name, attack, description, ammo, long_range):
        super(Sniper, self).__init__(name, attack, description, ammo)
        self.long_range = long_range


class Vehicle(Item):
    def __init__(self, name, description, transport):
        super(Vehicle, self).__init__(name, description)
        self.transport = transport


class Ship(Vehicle):
    def __init__(self, name, description, transport, space_travel):
        super(Ship, self).__init__(name, description, transport)
        self.space_travel = space_travel


class Sparrow(Vehicle):
    def __init__(self, name, description, transport, land_travel):
        super(Sparrow, self).__init__(name, description, transport)
        self.land_travel = land_travel


class Armor(Item):
    def __init__(self, name, description, defense):
        super(Armor, self).__init__(name, description)
        self.defense = defense


class Helmet(Armor):
    def __init__(self, name, description, defense, skull_protection):
        super(Helmet, self).__init__(name, description, defense)
        self.skull_protection = skull_protection