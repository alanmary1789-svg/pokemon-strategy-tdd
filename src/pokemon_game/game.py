class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def is_over(self):
        return (
            self.player1.pokemon.is_ko()
            or self.player2.pokemon.is_ko()
        )