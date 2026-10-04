from pokemon_game.pokemon import Pokemon
from pokemon_game.pokemon_type import PokemonType
from pokemon_game.potion import Potion


def test_potion_heals_pokemon():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    pikachu.take_damage(50)

    potion = Potion("Potion", 20)

    potion.use(pikachu)

    assert pikachu.hp == 70

def test_potion_cannot_heal_above_max_hp():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    pikachu.take_damage(10)

    potion = Potion("Super Potion", 50)

    potion.use(pikachu)

    assert pikachu.hp == 100