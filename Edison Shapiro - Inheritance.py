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