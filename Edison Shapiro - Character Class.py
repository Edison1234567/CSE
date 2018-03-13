class Character(object):
    def __init__(self, name, attack, death, take_damage, status_effect):
        self.name = name
        self.health = 120
        self.attack = attack
        self.death = death
        self.take_damage = take_damage
        self.paralyze = status_effect
        self.dialogue = True

    def name(self):
        print("name = Pikachu")
