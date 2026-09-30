from pokemon_game.pokemon import Pokemon 

def test_pokemon_starts_with_max_hp():
    pikachu = Pokemon("pikachu", 100)
    assert pikachu.hp == pikachu.max_hp

def test_pokemon_can_take_damage(): 
    pikachu = Pokemon("pikachu", 100)
    pikachu.take_damage(30)
    assert pikachu.hp == 70

def test_pokemon_hp_cannot_be_negative():
    pikachu = Pokemon("pikachu", 100)
    pikachu.take_damage(150)
    assert pikachu.hp == 0

def test_pokemon_is_ko_when_hp_reaches_zero():
    pikachu = Pokemon("Pikachu", 100)

    pikachu.take_damage(100)

    assert pikachu.is_ko()


def test_pokemon_is_not_ko_when_hp_remains():
    pikachu = Pokemon("Pikachu", 100)

    pikachu.take_damage(50)

    assert not pikachu.is_ko()

def test_pokemon_can_be_healed():
    pikachu = Pokemon("Pikachu", 100)
    pikachu.take_damage(40)

    pikachu.heal(20)

    assert pikachu.hp == 80


def test_pokemon_cannot_be_healed_above_max_hp():
    pikachu = Pokemon("Pikachu", 100)
    pikachu.take_damage(20)

    pikachu.heal(50)

    assert pikachu.hp == 100
