class Character(object):
    def __init__(self, name, attack, death, take_damage, use_item ):
        self.name = name
        self.health = 120
        self.attack = attack
        self.death = death
        self.take_damage = take_damage
        self.pick_up_items = True
        self.use_item = use_item

    def join_game(self):
        print("the game is starting")
        


