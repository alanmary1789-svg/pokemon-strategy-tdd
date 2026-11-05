from pokemon_game.player import Player


class ComputerPlayer(Player):

    def __init__(self, name, pokemon, attack_strategy, potions=None):
        super().__init__(name, pokemon, potions)
        self.attack_strategy = attack_strategy

    def choose_attack(self, opponent, battle):
        return self.attack_strategy.choose_attack(
            self.pokemon,
            opponent,
            battle
        )