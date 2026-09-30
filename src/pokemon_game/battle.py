from pokemon_game.damage_strategy import DamageStrategy

class Battle:
    def __init__(self, damage_strategy : DamageStrategy):
        self.damage_strategy = damage_strategy

    def attack(self, attacker, defender, attack):
        damage = self.damage_strategy.calculate(attack, attacker, defender)
        defender.take_damage(damage)

        