from pokemon_game.attack_strategy import (
    RandomAttackStrategy,
    StrongestAttackStrategy,
    EffectiveAttackStrategy,
)


def choose_difficulty():
    strategies = {
        "1": RandomAttackStrategy,
        "2": StrongestAttackStrategy,
        "3": EffectiveAttackStrategy,
    }

    labels = {
        "1": "Facile",
        "2": "Moyen",
        "3": "Difficile",
    }

    print("=== Pokémon Battle ===")
    print()
    print("Choisissez la difficulté :")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")

    while True:
        choice = input("> ")

        if choice in strategies:
            print(f"Difficulté sélectionnée : {labels[choice]}")
            return strategies[choice]()

        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")