from pokemon_game.pokemon import Pokemon
from pokemon_game.attack import Attack 
from pokemon_game.pokemon_type import PokemonType, TYPE_EFFECTIVENESS
from pokemon_game.damage_strategy import ContextDamageStrategy

def test_attack_has_name_and_damage_and_type():
    attack = Attack("Foudre", 20, PokemonType.ELECTRIC)

    assert attack.name == "Foudre"
    assert attack.damage == 20
    assert attack.type == PokemonType.ELECTRIC

"""
def test_pokemon_can_attack_another_pokemon():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)
    thunder_shock = Attack("Thunder Shock", 20, PokemonType.ELECTRIC)

    pikachu.attack(bulbasaur, thunder_shock, ContextDamageStrategy())

    assert bulbasaur.hp == 90
"""


