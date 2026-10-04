from pokemon_game.game import Game
from pokemon_game.player import Player
from pokemon_game.pokemon import Pokemon
from pokemon_game.pokemon_type import PokemonType
from pokemon_game.attack import Attack 


def test_game_is_over_when_a_pokemon_is_ko():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)

    player1 = Player("Alan", pikachu)
    player2 = Player("Opponent", bulbasaur)

    game = Game(player1, player2)

    bulbasaur.take_damage(100)

    assert game.is_over()

def test_game_is_not_over_while_both_pokemon_are_alive():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)

    player1 = Player("Alan", pikachu)
    player2 = Player("Opponent", bulbasaur)

    game = Game(player1, player2)

    assert not game.is_over()

def test_pokemon_can_have_attacks():
    thunderbolt = Attack(
        "Thunderbolt",
        20,
        PokemonType.ELECTRIC
    )

    pikachu = Pokemon(
        "Pikachu",
        100,
        PokemonType.ELECTRIC,
        [thunderbolt]
    )

    assert pikachu.attacks == [thunderbolt]

def test_pokemon_has_no_attacks_by_default():
    pikachu = Pokemon(
        "Pikachu",
        100,
        PokemonType.ELECTRIC
    )

    assert pikachu.attacks == []