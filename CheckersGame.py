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

    def get_condition(self):
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
        self.game_turn = 1
        self.board = [
                (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
                (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
                (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6),
                (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
                (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
                (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2),
                (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)
            ]

    def append_player_list(self, player: object):
        """
        This method updates the Checkers object players list with the player objects once created
        """
        self._players.append(player)

    def get_player_list(self):
        return self._players

    def print_board(self):

        players_list = self._players
        for row in range(8):
            for column in range(8):
                piece_pop = False
                for player in players_list:
                    for pieces in player.get_pieces_list():
                        if pieces.get_location() == (column + 1, 8 - row):
                            print("|", pieces.get_color(), end=" |")
                            piece_pop = True
                            continue
                    if piece_pop:
                        continue
                if not piece_pop:
                    print("|", None, end=" |")
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

    def play_game(self, player_name: str, starting_location: tuple, destination_location: tuple):
        """
        This method will allow the players to play the game
        :param player_name: The unique player name to identify the player making the move
        :param starting_location: The location of the piece the player wishes to move
        :param destination_location: The location the player wants to move their piece to
        :return:
        """

        # Check to make sure given player name exists
        players_list = self._players
        for player in players_list:
            if player.get_name() == player_name:
                current_player = player
                break
        else:
            raise InvalidPlayer("There is no player by this name")

        # check to make sure it is the given player's turn
        player_color_comparison = current_player.get_color()
        while self.game_turn % 2 != 0:
            if player_color_comparison == "White":
                raise OutOfTurn("It's not your turn!")
            else:
                break
        while self.game_turn % 2 == 0:
            if player_color_comparison == "Black":
                raise OutOfTurn("It's not your turn!")

        # add turn for next player
        self.game_turn += 1

        # Checking the player's pieces to make sure there is one at starting location
        player_pieces = current_player.get_pieces_list()
        for pieces in player_pieces:
            if pieces.get_location() == starting_location:
                current_piece = pieces
                break
        else:
            raise InvalidSquare("You don't have a piece on this square")

        # Check whether piece is normal, king, or triple king, decide whether destination location is a legal move
        # Move logic
        # Unplayable squares
        for x, y in destination_location:
            if y % 2 == 0 and x % 2 != 0:
                InvalidSquare("This is not a playable square")
            elif y % 2 != 0 and x % 2 == 0:
                InvalidSquare("This is not a playable square")
            elif x > 8 or y > 8:
                InvalidSquare("This square is outside of the 8x8 coordinates")
            elif x < 1 or y < 1:
                InvalidSquare("There are no square coordinates less than 1")
        # Rules applying to all pieces
        if starting_location == destination_location:
            InvalidSquare("This is not a legal move")
        # logic for black piece moves
        while current_piece.get_color() == "Black":
            # Condition 0 is a normal piece
            if current_piece.get_condition() == 0:
                for i, j in starting_location:
                    for x, y in destination_location:
                        if y - j <= 0:
                            raise InvalidSquare("Your piece can't move this way, it must move forward")
                        elif x == i and y - j < 4:
                            raise InvalidSquare("You must move diagonally")


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
    Kings and Triple Kings, and pieces captured. The pieces for each player are initialized automatically when each
    player is created
    """

    def __init__(self, player_name, piece_color):
        self._player_name = player_name
        self._piece_color = piece_color
        self._pieces = []
        self._captured_pieces = 0

        # This block of code populates the checkers board with the correct starting positions per piece color
        pieces_list = self._pieces
        row = [1, 2, 3, 4, 5, 6, 7, 8]
        while piece_color == "Black":
            for i in row[::2]:
                pieces_list.append(Piece(piece_color, (i, 3)))
                pieces_list.append(Piece(piece_color, (i, 1)))
            for i in row[1::2]:
                pieces_list.append(Piece(piece_color, (i, 2)))

        while piece_color == "White":
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
game.print_board()
game.play_game("Dan", (1, 1), (2, 2))
