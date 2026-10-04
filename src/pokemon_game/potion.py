class Potion:
    def __init__(self, name: str, heal_amount: int):
        self.name = name
        self.heal_amount = heal_amount

    def use(self, pokemon):
        pokemon.heal(self.heal_amount)