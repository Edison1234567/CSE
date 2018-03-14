class Character(object):
    def __init__(self, name, attack, death, take_damage, use_item, gun, sword, armor):
        self.name = name
        self.health = 120
        self.attack = attack
        self.gun = gun
        self.sword = sword
        self.armor = armor

    def take_damage(self, amt):
        self.health -= amt

    def attack(self, player):
        player.take_damage(self.attack)

        


