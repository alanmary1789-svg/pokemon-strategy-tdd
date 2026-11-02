from pokemon_game.pokemon import Pokemon 
from pokemon_game.pokemon_type import PokemonType, TYPE_EFFECTIVENESS
from pokemon_game.damage_strategy import ContextDamageStrategy
from pokemon_game.attack import Attack
from pokemon_game.game import Game
from pokemon_game.player import Player
from pokemon_game.battle import Battle

def test_pokemon_starts_with_max_hp():
    pikachu = Pokemon("pikachu", 100, PokemonType.ELECTRIC)
    assert pikachu.hp == pikachu.max_hp

def test_pokemon_can_take_damage(): 
    pikachu = Pokemon("pikachu", 100, PokemonType.ELECTRIC)
    pikachu.take_damage(30)
    assert pikachu.hp == 70

def test_pokemon_hp_cannot_be_negative():
    pikachu = Pokemon("pikachu", 100, PokemonType.ELECTRIC)
    pikachu.take_damage(150)
    assert pikachu.hp == 0

def test_pokemon_is_ko_when_hp_reaches_zero():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)

    pikachu.take_damage(100)

    assert pikachu.is_ko()


def test_pokemon_is_not_ko_when_hp_remains():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)

    pikachu.take_damage(50)

    assert not pikachu.is_ko()

def test_pokemon_can_be_healed():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    pikachu.take_damage(40)

    pikachu.heal(20)

    assert pikachu.hp == 80


def test_pokemon_cannot_be_healed_above_max_hp():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    pikachu.take_damage(20)

    pikachu.heal(50)

    assert pikachu.hp == 100


"""
def test_pokemon_attack_uses_damage_strategy():
    charmander = Pokemon("Charmander", 100, PokemonType.FIRE)
    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)

    strategy = ContextDamageStrategy()
    ember = Attack("Ember", 20, PokemonType.FIRE)

    charmander.attack(bulbasaur, ember, strategy)

    assert bulbasaur.hp == 60

"""

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
        Battle(ContextDamageStrategy())
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
        Battle(ContextDamageStrategy())
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