from pokemon_game.pokemon import Pokemon
from pokemon_game.attack import Attack
from pokemon_game.pokemon_type import PokemonType
from pokemon_game.damage_strategy import TypeDamageStrategy
from pokemon_game.battle import Battle

def test_battle_applies_damage_strategy():
    charmander = Pokemon("Charmander", 100, PokemonType.FIRE)
    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)
    ember = Attack("Ember", 20, PokemonType.FIRE)

    strategy = TypeDamageStrategy()
    battle = Battle(strategy)

    battle.attack(charmander, bulbasaur, ember)

    assert bulbasaur.hp == 60