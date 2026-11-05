from pokemon_game.pokemon_type import TYPE_EFFECTIVENESS
from pokemon_game.weather import WEATHER_EFFECTIVENESS
from pokemon_game.terrain import TERRAIN_EFFECTIVENESS


class DamageCalculator:

    def calculate(self, attack, attacker, defender, context):
        type_multiplier = TYPE_EFFECTIVENESS[attack.type].get(
            defender.type, 1
        )

        weather_multiplier = WEATHER_EFFECTIVENESS[context.weather].get(
            attack.type, 1
        )

        terrain_multiplier = TERRAIN_EFFECTIVENESS[context.terrain].get(
            attack.type, 1
        )

        return (
            attack.damage
            * type_multiplier
            * weather_multiplier
            * terrain_multiplier
        )