from pokemon_game.battle import Battle


class Game:
    def __init__(self, player1, player2, battle):
        self.player1 = player1
        self.player2 = player2
        self.battle = battle

    def is_over(self):
        return (
            self.player1.pokemon.is_ko()
            or self.player2.pokemon.is_ko()
        )

    def play(self):
        current_player = self.player1
        opponent = self.player2

        while not self.is_over():
            print()
            print(f"--- Tour de {current_player.name} ---")
            print(
                f"{current_player.pokemon.name}: "
                f"{current_player.pokemon.hp}/{current_player.pokemon.max_hp} HP"
            )
            print(
                f"{opponent.pokemon.name}: "
                f"{opponent.pokemon.hp}/{opponent.pokemon.max_hp} HP"
            )

            print("1. Attaquer")
            print("2. Utiliser une potion")

            choice = input("> ")

            if choice == "1":
                action_successful = self.choose_attack(current_player, opponent)

            elif choice == "2":
                action_successful = self.use_potion(current_player)

            else:
                print("Choix invalide.")
                continue

            if not action_successful:
                continue

            if self.is_over():
                break

            current_player, opponent = opponent, current_player
        self.display_winner()


    def choose_attack(self, current_player, opponent):
        pokemon = current_player.pokemon

        if not pokemon.attacks:
            print("Ce Pokémon ne possède aucune attaque.")
            return False

        print("Choisis une attaque :")

        for index, attack in enumerate(pokemon.attacks, start=1):
            print(f"{index}. {attack.name}")

        choice = input("> ")

        try:
            index = int(choice) - 1
        except ValueError:
            print("Veuillez entrer un nombre.")
            return False

        if not 0 <= index < len(pokemon.attacks):
            print("Cette attaque n'existe pas.")
            return False

        attack = pokemon.attacks[index]

        print(f"{pokemon.name} utilise {attack.name} !")

        self.battle.attack(
            pokemon,
            opponent.pokemon,
            attack
        )

        return True

    def use_potion(self, player):
        if not player.potions:
            print("Aucune potion disponible.")
            return False

        potion = player.potions[0]

        try:
            player.use_potion(potion)
        except ValueError as error:
            print(error)
            return False 

        print(f"{player.pokemon.name} utilise {potion.name}")
        return True

    def display_winner(self):
        if self.player1.pokemon.is_ko():
            winner = self.player2
        else:
            winner = self.player1

        print()
        print(f"{winner.name} gagne le combat !")