class InvalidPlayer(Exception):
    pass

class OutOfTurn(Exception):
    pass

class InvalidSquare(Exception):
    pass


class Checkers:
    def __init__(self, players):
        self._players = players
        captured_pieces = 0


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

    def play_game(self, player_name, starting_square_location, destination_square_location):

        if player.turn == False:
            raise OutOfTurn("It's not your turn!")

        if piece in starting_square_location is not player.piece: # does not belong to player
            raise InvalidSquare("The piece in this square isn't yours")

    def print_capture_pieces(self):
        return captured_pieces

    def get_checker_details(self, location: tuple):

        return checker_color  #check color based on player

        # needs to return if king or triple king

    def print_board(self):
        # print the board as an array
        pass

    def game_winner(self):
        # needs to return the game winner or if ther game is still going return that
        pass



class Player:

    def __init__(self, player_name, checker_color):
        self._player_name = player_name
        self._checker_color = checker_color
        king_count = 0
        triple_king_count = 0

    def get_king_count(self):
        return king_count


    def get_triple_king_count(self):
        return triple_king_count

    def get_captured_pieces_count(self):
        return captured_pieces








