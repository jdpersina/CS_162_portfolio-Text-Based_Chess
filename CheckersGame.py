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
    def __init__(self, color: str, location: tuple):
        self._color = color
        self._location = location
        self._condition = 0

    def king_counts(self):
        """
        This method shows whether the piece is normal, king, or a triple king
        """
        return self._condition

    def get_location(self):
        """
        This method shows the piece's location on the board
        """
        return self._location

    def get_color(self):
        return self._color

    def return_condition(self, location: tuple):
        return self._condition


class Checkers:
    """
    The checkers class will have a method to create the players for the checkers game (This method will create
    the player class) with parameters for player name and piece color, and a method to play the game, with the
    parameters player name, starting square, and destination square. The latter two parameters being tuple coordinates
    which the player will use to determine which piece the player wants to move and where to move it
    """

    def __init__(self):
        self._players = []
        #self.board = [
                #(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
                #(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
                #(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6),
                #(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
                #(1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                #(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
                #(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2),
                #(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)
            #]

    def append_player_list(self, player: object):
        """
        This method updates the Checkers object players list with the player objects once created
        """
        self._players.append(player)

    def print_board(self):

        for row in range(8):
            for col in range(8):
                piece_found = False
                for player in self._players:
                    for piece in player.get_pieces_list():
                        if piece.get_location() == (col + 1, 8 - row):
                            print("|", piece.get_color(), end=" |")
                            piece_found = True
                            break
                    if piece_found:
                        break
                if not piece_found:
                    print("| None", end=" |")
            print()

    def create_player(self, player_name: str, piece_color: str):
        """
        A function which creates a player object for the checkers game. There must be only two players per game with
        checkers pieces being either black or white. The player who chooses black will have the first turn
        :param player_name: must be at least one discernible character, must be unique to the player
        :param piece_color: must be "White" or "Black"
        """
        # Check to make sure player chose a discernible name
        if player_name == "":
            raise InvalidPlayer("You must choose a name")
        # Check to make sure player chose one of the two allowed piece colors, black or white
        if piece_color != 'White':
            if piece_color != 'Black':
                raise InvalidPlayer("Your piece color must be Black or White")

        # This block compares the second player's name and piece color to the first player's to make sure they're unique
        for player in self._players:

            first_player_name = player.get_name()
            first_player_color = player.get_color()

            if first_player_name == player_name:
                raise InvalidPlayer("The player names must be unique")

            if first_player_color == piece_color:
                raise InvalidPlayer("The other player has already chosen this color")

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

        if self._players.turn == False:
            raise OutOfTurn("It's not your turn!")

        if piece in starting_square_location is not player.piece: # does not belong to player
            raise InvalidSquare("The piece in this square isn't yours")
        pass

    def print_captured_pieces(self):
        """
        This method will return the amount of pieces the given player has captured
        """
        return Player.get_captured_pieces_count()

    def get_checker_details(self, location: tuple):
        """
        This method will return information on piece color and King or Triple King status for the given checker piece
        :param location: a tuple to tell the method where the piece to be checked is located
        """
        return checker_color  #check color based on player
        pass

        # needs to return if king or triple king

    def print_board(self):
        """
        This method will print the entire board as an array to give players a visualization of the current game
        """
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
        self._captured_pieces = 0

        # This block of code populates the checkers board with the correct starting positions per piece color
        pieces_list = self._pieces
        row = [1, 2, 3, 4, 5, 6, 7, 8]
        if piece_color == "Black":
            for i in row[::2]:
                pieces_list.append(Piece(piece_color, (i, 3)))
                pieces_list.append(Piece(piece_color, (i, 1)))
            for i in row[1::2]:
                pieces_list.append(Piece(piece_color, (i, 2)))

        if piece_color == "White":
            for i in row[::2]:
                pieces_list.append(Piece(piece_color, (i, 7)))
            for i in row[1::2]:
                pieces_list.append(Piece(piece_color, (i, 8)))
                pieces_list.append(Piece(piece_color, (i, 6)))

    def get_pieces_list(self):
        return self._pieces

    def get_name(self):
        return self._player_name

    def get_color(self):
        return self._piece_color

    def get_king_count(self):
        """
        This method will return the number of Kings the player has on the board, it won't count captured kings
        """
        king_count = 0
        for pieces in self._pieces:
            if pieces.king_counts() == 1:
                king_count += 1
        return king_count

    def get_triple_king_count(self):
        """
        This method will return the number of triple Kings the player has on the board, it won't count captured
        triple kings
        """
        trip_king_count = 0
        for pieces in self._pieces:
            if pieces.king_counts() == 2:
                trip_king_count += 1
        return trip_king_count

    def get_captured_pieces_count(self):
        """
        This method will return the number of pieces the given player has captured
        """
        return self._captured_pieces


game = Checkers()
p1 = game.create_player("Dan", "Black")
p2 = game.create_player("Darcie", "White")
print(game.print_board())
