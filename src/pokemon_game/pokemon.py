class Pokemon:
    hp : int

    def __init__(self, name : str, max_hp : int):
        self.max_hp = max_hp
        self.name = name 
        self.hp = max_hp

    def take_damage(self, damage : int):
        if self.hp > damage :
            self.hp -= damage
        else : 
            self.hp = 0


    def is_ko(self):
        return self.hp == 0 

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp :
            self.hp = self.max_hp 


