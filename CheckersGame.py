class InvalidPlayer(Exception):
    pass


class Checkers:
    def __init__(self, players):
        self._players = players

    def create_player(self, player_name, piece_color):
        """
        This is a function which creates a player object for the checkers game.
        """
        for players in self._players:
            if player_name == self._players:
                raise InvalidPlayer("The player names must be unique")
            elif player_name is None:
                raise InvalidPlayer("You must choose a name")

        if piece_color != "White" or piece_color != "Black":
            raise InvalidPlayer("Your piece color must be Black or White")
