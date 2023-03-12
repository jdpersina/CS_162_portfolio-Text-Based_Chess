class InvalidPlayer(Exception):
    """
    Exception to raise when a player name or checker color is incorrect
    """
    pass

class OutOfTurn(Exception):
    """
    Exception to raise when player attempts a move out of turn
    """
    pass

class InvalidSquare(Exception):
    """
    Exception to raise when player attempts to move a piece from a square that isn't their piece or doesn't have a piece
    """
    pass

class Piece:
    def __init__(self, color, location: tuple):
        self._color = color
        self._location = location
        self._condition = 0

class Checkers:
    """
    The checkers class will have a method to create the players for the checkers game (This method will create
    the player class) with parameters for player name and piece color, and a method to play the game, with the
    parameters player name, starting square, and destination square. The latter two parameters being tuple coordinates
    which the player will use to determine which piece the player wants to move and where to move it
    """

    def __init__(self, players: list = None):
        self._players = players
        self.turn_counter = 0
        self._board = [
                [(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)],
                [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)],
                [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)],
                [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)],
                [(1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)],
                [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)],
                [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)],
                [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]
            ]

        # working on board setting, probably won't go here, maybe goes in create player method
        while self.turn_counter == 0:
            for rows in self._board:
                for (x,y) in rows:
                    if x % 2 == 0 and y <= 3:


    def create_player(self, player_name: str, piece_color: str):
        """
        A function which creates a player object for the checkers game. There must be only two players per game with
        checkers pieces being either black or white. The player who chooses black will have the first turn
        :param player_name: must be at least one discernible character, must be unique to the player
        :param piece_color: must be "White" or "Black"
        """
        for players in self._players:
            if player_name == self._players:
                raise InvalidPlayer("The player names must be unique")
            elif player_name is None:
                raise InvalidPlayer("You must choose a name")

            if piece_color == self._players:
                raise InvalidPlayer("The other player has already chosen this color")

        if piece_color != "White" or piece_color != "Black":
            raise InvalidPlayer("Your piece color must be Black or White")

        self._players.append(Player(player_name, piece_color))
        return Player(player_name, piece_color)

    def play_game(self, player_name: str, starting_square_location: tuple, destination_square_location: tuple):
        """
        This method will allow the players to play the game
        :param player_name: The unique player name to identify the player making the move
        :param starting_square_location: The location of the piece the player wishes to move
        :param destination_square_location: The location the player wants to move their piece to
        :return:
        """

        if self._player.turn == False:
            raise OutOfTurn("It's not your turn!")

        if piece in starting_square_location is not player.piece: # does not belong to player
            raise InvalidSquare("The piece in this square isn't yours")

    def print_captured_pieces(self):
        """
        This method will return the amount of pieces the given player has captured
        """
        return Player.get_captured_pieces_count

    def get_checker_details(self, location: tuple):
        """
        This method will return information on King or Triple King status for the given checkers piece
        :param location: a tuple to tell the method where the piece to be checked is located
        """
        return checker_color  #check color based on player

        # needs to return if king or triple king

    def print_board(self):
        """
        This method will print the entire board as an array to give players a visualization of the current game
        """
        while Checkers is True:

        # print the board as an array
        pass

    def game_winner(self):
        """
        This method will either return the winner of the game or if the game hasn't ended yet, it will indicate so
        """
        # needs to return the game winner or if the game is still going return that
        pass



class Player:
    """
    This class will create Player objects, of which there are two per game. It will be initialized by the create_player
    method in the Checkers class. This object will store player information including name, piece color, the number of
    Kings and Triple Kings, and pieces captured
    """

    def __init__(self, player_name, piece_color):
        self._player_name = player_name
        self._piece_color = piece_color
        self._pieces = []
        self._king_count = 0
        self._triple_king_count = 0
        self._captured_pieces = 0

    def piece(self,):

    def get_king_count(self):
        """
        This method will return the number of Kings the player has on the board, it won't count captured kings
        """
        return self._king_count

    def get_triple_king_count(self):
        """
        This method will return the number of triple Kings the player has on the board, it won't count captured
        triple kings
        """
        return self._triple_king_count

    def get_captured_pieces_count(self):
        """
        This method will return the number of pieces the given player has captured
        """
        return self._captured_pieces
