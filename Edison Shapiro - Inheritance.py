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


class Pulse_Rifle(Gun):
    