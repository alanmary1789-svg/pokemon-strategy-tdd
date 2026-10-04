from pokemon_game.player import Player
from pokemon_game.pokemon import Pokemon
from pokemon_game.pokemon_type import PokemonType
from pokemon_game.potion import Potion


def test_player_can_have_potions():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    potion = Potion("Potion", 20)

    player = Player("Alan", pikachu, [potion])

    assert player.pokemon == pikachu
    assert player.potions == [potion]

def test_player_uses_and_consumes_potion():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    pikachu.take_damage(50)

    potion = Potion("Potion", 20)
    player = Player("Alan", pikachu, [potion])

    player.use_potion(potion)

    assert pikachu.hp == 70
    assert potion not in player.potions