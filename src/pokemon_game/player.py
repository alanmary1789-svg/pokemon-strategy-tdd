class Player:
    def __init__(self, name, pokemon, potions=None):
        self.name = name
        self.pokemon = pokemon
        self.potions = potions if potions is not None else []

    def use_potion(self, potion):
        if potion not in self.potions :
            raise ValueError("Potion absent de l'inventaire")

        if self.pokemon.hp == self.pokemon.max_hp:
            raise ValueError("Ce Pokémon possède déjà tous ses PV ")
        
        potion.use(self.pokemon)
        self.potions.remove(potion)

    