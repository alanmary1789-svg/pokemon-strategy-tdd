from pokemon_game.game import Game
from pokemon_game.player import Player
from pokemon_game.pokemon import Pokemon
from pokemon_game.pokemon_type import PokemonType
from pokemon_game.attack import Attack 
from pokemon_game.battle import Battle 
from pokemon_game.damage_calculator import DamageCalculator
from pokemon_game.potion import Potion


def test_game_is_over_when_a_pokemon_is_ko():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)

    player1 = Player("Alan", pikachu)
    player2 = Player("Opponent", bulbasaur)

    game = Game(player1, player2, Battle(DamageCalculator()))

    bulbasaur.take_damage(100)

    assert game.is_over()

def test_game_is_not_over_while_both_pokemon_are_alive():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)

    player1 = Player("Alan", pikachu)
    player2 = Player("Opponent", bulbasaur)

    game = Game(player1, player2, Battle(DamageCalculator()))

    assert not game.is_over()


    assert pikachu.attacks == []

def test_invalid_attack_choice_does_not_crash(monkeypatch):
    pikachu = Pokemon(
        "Pikachu",
        100,
        PokemonType.ELECTRIC,
        [Attack("Thunderbolt", 20, PokemonType.ELECTRIC)]
    )

    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)

    player1 = Player("Alan", pikachu)
    player2 = Player("Opponent", bulbasaur)

    game = Game(
        player1,
        player2,
        Battle(DamageCalculator())
    )

    monkeypatch.setattr("builtins.input", lambda _: "abc")

    result = game.choose_attack(player1, player2)

    assert result is False
    assert bulbasaur.hp == 100

def test_using_potion_at_full_hp_does_not_consume_turn():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)

    potion = Potion("Potion", 20)

    player1 = Player("Alan", pikachu, [potion])
    player2 = Player("Opponent", bulbasaur)

    game = Game(
        player1,
        player2,
        Battle(DamageCalculator())
    )

    result = game.use_potion(player1)

    assert result is False
    assert pikachu.hp == 100
    assert potion in player1.potions

def test_invalid_action_does_not_skip_player_turn(monkeypatch):
    thunderbolt = Attack("Thunderbolt", 20, PokemonType.ELECTRIC)
    ember = Attack("Ember", 100, PokemonType.FIRE)

    pikachu = Pokemon(
        "Pikachu", 100, PokemonType.ELECTRIC, [thunderbolt]
    )
    charmander = Pokemon(
        "Charmander", 100, PokemonType.FIRE, [ember]
    )

    player1 = Player("Alan", pikachu)
    player2 = Player("Opponent", charmander)

    game = Game(
        player1,
        player2,
        Battle(DamageCalculator())
    )

    # Alan saisit une action invalide, puis attaque.
    # Ensuite, l'adversaire attaque et termine le combat.
    inputs = iter(["abc", "1", "1", "1", "1"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    game.play()

    assert charmander.hp == 80
    assert pikachu.is_ko()


def test_invalid_attack_selection_does_not_skip_turn(monkeypatch):
    thunderbolt = Attack("Thunderbolt", 20, PokemonType.ELECTRIC)
    ember = Attack("Ember", 100, PokemonType.FIRE)

    pikachu = Pokemon(
        "Pikachu", 100, PokemonType.ELECTRIC, [thunderbolt]
    )
    charmander = Pokemon(
        "Charmander", 100, PokemonType.FIRE, [ember]
    )

    player1 = Player("Alan", pikachu)
    player2 = Player("Opponent", charmander)

    game = Game(
        player1,
        player2,
        Battle(DamageCalculator())
    )

    # Alan choisit Attaquer, puis une attaque inexistante.
    # Il peut ensuite recommencer son tour.
    inputs = iter(["1", "99", "1", "1", "1", "1"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    game.play()

    assert charmander.hp == 80
    assert pikachu.is_ko()

def test_game_stops_immediately_after_ko(monkeypatch, capsys):
    thunderbolt = Attack("Thunderbolt", 100, PokemonType.ELECTRIC)

    pikachu = Pokemon(
        "Pikachu",
        100,
        PokemonType.ELECTRIC,
        [thunderbolt]
    )

    charmander = Pokemon(
        "Charmander",
        100,
        PokemonType.FIRE
    )

    player1 = Player("Alan", pikachu)
    player2 = Player("Opponent", charmander)

    game = Game(
        player1,
        player2,
        Battle(DamageCalculator())
    )

    inputs = iter(["1", "1"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    game.play()

    output = capsys.readouterr().out

    assert charmander.is_ko()
    assert pikachu.hp == 100
    assert "Alan gagne le combat !" in output
    assert "--- Tour de Opponent ---" not in output

from pokemon_game.computer_player import ComputerPlayer
from pokemon_game.attack_strategy import StrongestAttackStrategy
from pokemon_game.damage_calculator import DamageCalculator

def test_computer_player_attacks_without_user_input(monkeypatch, capsys):
    thunderbolt = Attack("Thunderbolt", 20, PokemonType.ELECTRIC)
    ember = Attack("Ember", 100, PokemonType.FIRE)

    pikachu = Pokemon(
        "Pikachu",
        100,
        PokemonType.ELECTRIC,
        [thunderbolt]
    )

    charmander = Pokemon(
        "Charmander",
        100,
        PokemonType.FIRE,
        [ember]
    )

    human = Player("Alan", pikachu)

    computer = ComputerPlayer(
        "Adversaire",
        charmander,
        StrongestAttackStrategy()
    )

    game = Game(
        human,
        computer,
        Battle(DamageCalculator())
    )

    # Les seules saisies autorisées sont celles du joueur humain.
    inputs = iter(["1", "1"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    game.play()

    output = capsys.readouterr().out

    assert pikachu.is_ko()
    assert charmander.hp == 80
    assert "Charmander utilise Ember !" in output

def test_choose_attack_displays_damage_and_remaining_hp(
    monkeypatch, capsys
):
    thunderbolt = Attack(
        "Thunderbolt", 20, PokemonType.ELECTRIC
    )

    pikachu = Pokemon(
        "Pikachu", 100, PokemonType.ELECTRIC, [thunderbolt]
    )

    squirtle = Pokemon(
        "Squirtle", 100, PokemonType.WATER
    )

    player1 = Player("Alan", pikachu)
    player2 = Player("Opponent", squirtle)

    game = Game(
        player1,
        player2,
        Battle(DamageCalculator())
    )

    monkeypatch.setattr("builtins.input", lambda _: "1")

    game.choose_attack(player1, player2)

    output = capsys.readouterr().out

    assert "Pikachu utilise Thunderbolt !" in output
    assert "Squirtle subit 40 dégâts !" in output
    assert "Squirtle : 60/100 PV" in output