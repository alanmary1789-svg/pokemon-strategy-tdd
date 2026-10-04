class Player:
    def __init__(self, name, pokemon, potions=None):
        self.name = name
        self.pokemon = pokemon
        self.potions = potions if potions is not None else []

    def use_potion(self, potion):
        potion.use(self.pokemon)
        self.potions.remove(potion)