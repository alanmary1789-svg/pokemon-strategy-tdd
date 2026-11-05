from pokemon_game.weather import Weather
from pokemon_game.battle import Battle
from pokemon_game.attack import Attack  
from pokemon_game.damage_calculator import DamageCalculator
from pokemon_game.pokemon import Pokemon, PokemonType

def test_battle_has_weather():
    calculator = DamageCalculator()
    battle = Battle(calculator, Weather.RAIN)

    assert battle.weather == Weather.RAIN 


def test_rain_halves_fire_damage():
    charmander = Pokemon("Charmander", 100, PokemonType.FIRE)
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)

    ember = Attack("Ember", 20, PokemonType.FIRE)

    calculator = DamageCalculator()
    battle = Battle(calculator, Weather.RAIN)

    battle.attack(charmander, pikachu, ember)
    assert pikachu.hp == 90

