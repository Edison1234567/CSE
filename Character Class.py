class Character(object):
    def __init__(self, name, attack, gun, sword, armor):
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

    def use_item(self, armor):
        self.use_item(armor)

    def death(self):
        if self.health == 0:
            print("You Died")