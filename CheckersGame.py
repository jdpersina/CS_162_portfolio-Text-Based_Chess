# Author: Joseph 'Dan' Persina
# GitHub username: jdpersina
# Date: 3/4/23
# Description: A checkers game with modified rules

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
    """
    The piece class has three attributes: Condition, which keeps track of whether the piece is normal, a King, or
    Triple King. Color, either Black or White in keeping with traditional checkers pieces colors, and a location on the
    board as a coordinate tuple. The pieces for each player are populated to the board automatically when the player for
    the given color is created.
    """
    def __init__(self, color: str, location: tuple):
        self._color = color
        self._location = location
        self._condition = 0

    def get_condition(self):
        """
        Condition coincides with whether the given piece is 0 = normal, 1 = King, or 2 = Triple King
        """
        return self._condition

    def condition_change(self):
        """
        This method will change the condition for the given piece, (0 = normal, 1 = King, 2 = Triple King) when the
        conditions for change are met
        """
        self._condition += 1

    def get_location(self):
        """
        This method shows the piece's location on the board
        """
        return self._location

    def change_location(self, new_coords):
        """
        This is a method to change the piece's coordinates
        :param new_coords: a tuple that gives the piece its new location after a legal move
        """
        self._location = new_coords

    def get_color(self):
        """
        This method will return the color of the given piece
        """
        return self._color


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

    def append_player_list(self, player: object):
        """
        This method updates the Checkers object players list with the player objects once created
        """
        self._players.append(player)

    def get_player_list(self):
        return self._players

    def check_coordinates(self, coordinates: tuple):
        for players in self._players:
            for pieces in players.get_pieces_list():
                if pieces.get_location() == coordinates:
                    if pieces.get_color() == "Black":
                        return "Black"
                    if pieces.get_color == "White":
                        return "White"

                elif pieces.get_location() != coordinates:
                    return None

    def print_board(self):

        players_list = self._players
        for row in reversed(range(8)):
            for column in range(8):
                piece_pop = False

                for player in players_list:
                    for pieces in player.get_pieces_list():
                        if pieces.get_location() == (column, row):
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
        # Keeping count of the pieces captured this turn
        captured_pieces = 0

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
            else:
                break

        # Checking the player's pieces to make sure there is one at starting location
        player_pieces = current_player.get_pieces_list()
        for pieces in player_pieces:
            if pieces.get_location() == starting_location:
                current_piece = pieces
                break
        else:
            raise InvalidSquare("You don't have a piece on this square")

        # Move logic
        # Unplayable squares
        x, y = destination_location
        # SQUARES WHICH PIECES CAN'T LAND ON
        if y % 2 != 0 and x % 2 == 0:
            raise InvalidSquare("This is not a playable square")
        if y % 2 == 0 and x % 2 != 0:
            raise InvalidSquare("This is not a playable square")

        # Squares that exist outside the 8x8 board
        if x > 7 or y > 7:
            raise InvalidSquare("There are no square coordinates greater than 7")
        if x < 0 or y < 0:
            raise InvalidSquare("There are no square coordinates less than 0")

        # Rules applying to all pieces
        if starting_location == destination_location:
            raise InvalidSquare("This is not a legal move")
        for players in self._players:
            for pieces in players.get_pieces_list():
                if pieces.get_location() == destination_location:
                    raise InvalidSquare("There is already a piece at this location")
                else:
                    continue

        # If player's move takes a piece, this will change to true, will print piece taken message at end of function
        piece_taken = False
        piece_taken_mess = "You took one of your opponent's pieces"

        # If player's piece changes to king or triple king, this will turn true and print the condition change message
        condition_change = False
        king_message = f"The piece at {destination_location} is now a King!"
        x3_king_message = f"The piece at {destination_location} is now a Triple King!"

        # Unpacking the tuples for start and destination
        i, j = starting_location
        x, y = destination_location

        # Check diagonal space around piece to see if there are other player's pieces around. Booleans, start False
        q_1_opposed_piece = False
        q_2_opposed_piece = False
        q_3_opposed_piece = False
        q_4_opposed_piece = False

        # Check diagonal space around piece to see if the same player's pieces are around. Booleans, start False
        q_1_team_piece = False
        q_2_team_piece = False
        q_3_team_piece = False
        q_4_team_piece = False

        # logic for black piece moves
        if current_piece.get_color() == "Black":
            # Condition 0 is a normal piece
            if current_piece.get_condition() == 0:
                quad_1 = (i - 1, j + 1)
                quad_2 = (i + 1, j + 1)
                q_1_op_mess = f"There is a piece at {quad_1} that you must jump"
                q_2_op_mess = f"There is a piece at {quad_2} that you must jump"
                team_mess = "You can't jump your own pieces"

                for player in self._players:
                    if player.get_color() == "White":
                        opposed_player = player
                        for pieces in opposed_player.get_pieces_list():
                            if pieces.get_location() == quad_1:
                                q_1_op = pieces
                                q_1_opposed_piece = True
                            if pieces.get_location() == quad_2:
                                q_2_op = pieces
                                q_2_opposed_piece = True

                    if player.get_color() == "Black":
                        same_player = player
                        for pieces in same_player.get_pieces_list():
                            if pieces.get_location() == quad_1:
                                q_1_team = pieces
                                q_1_team_piece = True
                            if pieces.get_location() == quad_2:
                                q_2_team = pieces
                                q_2_team_piece = True

                    # Team pieces on both possible moves
                    if q_1_team_piece and q_2_team_piece:
                        return "The piece you want to move doesn't have any legal moves"
                    # Trying to jump a team piece
                    elif q_1_team_piece and destination_location == (i - 2, j + 2):
                        return team_mess
                    # Trying to jump a team piece
                    elif q_2_team_piece and destination_location == (i + 2, j + 2):
                        return team_mess

                    # If trying to move in right direction when player can take an opposing piece
                    elif q_1_opposed_piece and not q_2_opposed_piece:
                        if destination_location == (i + 1, j + 1) and self.check_coordinates((i - 2, j + 2)) is None:
                            return q_1_op_mess
                    # If trying to move in left direction when player can take an opposing piece
                    elif q_2_opposed_piece and not q_1_opposed_piece:
                        if destination_location == (i - 1, j + 1) and self.check_coordinates((i + 2, j + 2)) is None:
                            return q_2_op_mess

                    # successful move, taking no pieces
                    elif destination_location == (i - 1, j + 1) or destination_location == (i + 1, j + 1):
                        current_piece.change_location(destination_location)

                    # successful move, capturing a piece
                    elif destination_location == (i - 2, j + 2):
                        opposed_player.remove_piece(q_1_op)
                        current_piece.change_location(destination_location)
                        piece_taken = True
                        captured_pieces += 1

                    elif destination_location == (i + 2, j + 2):
                        opposed_player.remove_piece(q_2_op)
                        current_piece.change_location(destination_location)
                        piece_taken = True
                        captured_pieces += 1

                    # Black piece change to king
                    if current_piece.get_condition() == 0 and y == 7:
                        condition_change = True
                    # Black piece change to Triple King
                    if current_piece.get_condition == 1 and y == 0:
                        condition_change = True

            if current_piece.get_condition() == 1:
                # Condition 1 is a normal piece
                if current_piece.get_condition() == 0:
                    quad_1 = (i - 1, j + 1)
                    quad_2 = (i + 1, j + 1)
                    quad_3 = (i - 1, j - 1)
                    quad_4 = (i + 1, j - 1)
                    q_1_op_mess = f"There is a piece at {quad_1} that you must jump"
                    q_2_op_mess = f"There is a piece at {quad_2} that you must jump"
                    q_3_op_mess = f"There is a piece at {quad_3} that you must jump"
                    q_4_op_mess = f"There is a piece at {quad_4} that you must jump"
                    team_mess = "You can't jump your own pieces"

        # Logic for White pieces
        if current_piece.get_color() == "White":
            # Condition 0 is a normal piece
            if current_piece.get_condition() == 0:
                # For condition 0 pieces, we only check the quadrants ahead of them
                quad_1 = (i - 1, j - 1)
                quad_2 = (i + 1, j - 1)

                # info messages when quadrants ahead of piece are populated
                q_1_op_mess = f"There is a piece at {quad_1} that you must jump"
                q_2_op_mess = f"There is a piece at {quad_2} that you must jump"
                team_mess = "You can't jump your own pieces"

                for player in self._players:
                    if player.get_color() == "Black":
                        opposed_player = player
                        for pieces in opposed_player.get_pieces_list():
                            if pieces.get_location() == quad_1:
                                q_1_op = pieces
                                q_1_opposed_piece = True
                            if pieces.get_location() == quad_2:
                                q_2_op = pieces
                                q_2_opposed_piece = True

                    if player.get_color() == "White":
                        same_player = player
                        for pieces in same_player.get_pieces_list():
                            if pieces.get_location() == quad_1:
                                q_1_team = pieces
                                q_1_team_piece = True
                            if pieces.get_location() == quad_2:
                                q_2_team = pieces
                                q_2_team_piece = True

                    # Team pieces on both possible moves
                    if q_1_team_piece and q_2_team_piece:
                        return "The piece you want to move doesn't have any legal moves"
                    # Trying to jump a team piece
                    elif q_1_team_piece and destination_location == (i - 2, j - 2):
                        return team_mess
                    # Trying to jump a team piece
                    elif q_2_team_piece and destination_location == (i + 2, j - 2):
                        return team_mess

                    # If trying to move in right direction when player can take an opposing piece
                    elif q_1_opposed_piece and not q_2_opposed_piece:
                        if destination_location == (i + 1, j - 1) and self.check_coordinates((i - 2, j - 2)) is None:
                            return q_1_op_mess
                    # If trying to move in left direction when player can take an opposing piece
                    elif q_2_opposed_piece and not q_1_opposed_piece:
                        if destination_location == (i - 1, j - 1) and self.check_coordinates((i + 2, j - 2)) is None:
                            return q_2_op_mess

                    # successful move, taking no pieces
                    elif destination_location == (i - 1, j - 1) or destination_location == (i + 1, j - 1):
                        current_piece.change_location(destination_location)

                    # successful move, taking a piece
                    elif destination_location == (i - 2, j - 2):
                        opposed_player.remove_piece(q_1_op)
                        current_piece.change_location(destination_location)
                        current_player.piece_captured()
                        piece_taken = True
                        captured_pieces += 1

                    # successful move, taking a piece
                    elif destination_location == (i + 2, j - 2):
                        opposed_player.remove_piece(q_2_op)
                        current_piece.change_location(destination_location)
                        current_player.piece_captured()
                        piece_taken = True
                        captured_pieces += 1

                    # White piece change to king
                    if current_piece.get_condition() == 0 and y == 0:
                        condition_change = True

                    # White piece change to Triple King
                    if current_piece.get_condition == 1 and y == 7:
                        condition_change = True

            # White piece change to King conditions
            if current_piece.get_condition() == 0 and y == 0:
                condition_change = True

            # White piece change to Triple King conditions
            if current_piece.get_condition == 1 and y == 7:
                condition_change = True

        if piece_taken and condition_change:
            if current_piece.get_condition() == 0:
                # Change to King
                current_piece.condition_change()

                # Check if there are more pieces to take
                # Only checking forward facing coordinates for each color since they're at the end of the board to ~
                #      ~ get condition change
                if current_player.get_color() == "Black":
                    if self.check_coordinates((x - 1, y - 1)) == opposed_player.get_color:
                        if self.check_coordinates((x - 2, y - 2)) is None:
                            return print(f"{piece_taken_mess} and {king_message}. It's still your turn")

                    elif self.check_coordinates((x + 1, y - 1)) == opposed_player.get_color:
                        if self.check_coordinates((x + 2, y - 2)) is None:
                            return print(f"{piece_taken_mess} and {king_message}. It's still your turn")

                if current_player.get_color() == "White":
                    if self.check_coordinates((x - 1, y + 1)) == opposed_player.get_color:
                        if self.check_coordinates((x - 2, y + 2)) is None:
                            return print(f"{piece_taken_mess} and {king_message}. It's still your turn")

                    if self.check_coordinates((x + 1, y + 1)) == opposed_player.get_color:
                        if self.check_coordinates((x + 2, y + 2)) is None:
                            return print(f"{piece_taken_mess} and {king_message}. It's still your turn")

                    # No more pieces to jump
                    else:
                        self.game_turn += 1
                        return print(f"{piece_taken_mess} and {king_message}")

            elif current_piece.get_condition == 1:
                # Change to Triple King
                current_piece.condition_change()

                # check if there are more pieces to take
                # Only checking forward facing coordinates for each color since they're at the end of the board to ~
                #      ~ get condition change
                if current_player.get_color() == "Black":
                    if self.check_coordinates((x - 1, y + 1)) == opposed_player.get_color:
                        if self.check_coordinates((x - 2, y + 2)) is None:
                            return print(f"{piece_taken_mess} and {x3_king_message}. It's still your turn")

                    elif self.check_coordinates((x + 1, y + 1)) == opposed_player.get_color:
                        if self.check_coordinates((x + 2, y + 2)) is None:
                            return print(f"{piece_taken_mess} and {x3_king_message}. It's still your turn")

                if current_player.get_color() == "White":
                    if self.check_coordinates((x - 1, y - 1)) == opposed_player.get_color:
                        if self.check_coordinates((x - 2, y - 2)) is None:
                            return print(f"{piece_taken_mess} and {x3_king_message}. It's still your turn")

                    elif self.check_coordinates((x + 1, y - 1)) == opposed_player.get_color:
                        if self.check_coordinates((x + 2, y - 2)) is None:
                            return print(f"{piece_taken_mess} and {x3_king_message}. It's still your turn")

                    # No more pieces to jump
                    else:
                        self.game_turn += 1
                        return print(f"{piece_taken_mess} and {x3_king_message}")

        if piece_taken:
            # check if there are more pieces to take
            if self.check_coordinates((x - 1, y + 1)) == opposed_player.get_color:
                if self.check_coordinates((x - 2, y + 2)) is None:
                    return print(f"{piece_taken_mess}. It's still your turn")

            elif self.check_coordinates((x + 1, y + 1)) == opposed_player.get_color:
                if self.check_coordinates((x + 2, y + 2)) is None:
                    return print(f"{piece_taken_mess}. It's still your turn")

            elif self.check_coordinates((x - 1, y - 1)) == opposed_player.get_color:
                if self.check_coordinates((x - 2, y - 2)) is None:
                    return print(f"{piece_taken_mess}. It's still your turn")

            elif self.check_coordinates((x + 1, y - 1)) == opposed_player.get_color:
                if self.check_coordinates((x + 2, y - 2)) is None:
                    return print(f"{piece_taken_mess}. It's still your turn")

                # No more pieces to jump
                else:
                    self.game_turn += 1
                    return print(f"{piece_taken_mess} and your piece is now at {destination_location}")

        # Condition Change only
        if condition_change:
            # Normal to king
            if current_piece.get_condition() == 0:
                current_piece.condition_change()
                self.game_turn += 1
                return print(f"{king_message}")

            # King to Triple King
            elif current_piece.get_condition == 1:
                current_piece.condition_change()
                self.game_turn += 1
                return print(f"{x3_king_message}")

        # No pieces taken and no condition change
        if not piece_taken and not condition_change:
            self.game_turn += 1
            return print(f"your piece is now at {destination_location}")

    def get_checker_details(self, location: tuple):
        """
        This method will return information on piece color and King or Triple King status for the given checker piece
        :param location: a tuple to tell the method where the piece to be checked is located
        """
        x, y = location
        if x > 7 or y > 7:
            raise InvalidSquare("This square doesn't exist")
        if x < 0 or y < 0:
            raise InvalidSquare("This square doesn't exist")

        for players in self._players:
            for pieces in players.get_pieces_list():
                if pieces.get_location == location:
                    info_piece = pieces

                    if info_piece.get_color() == "Black":
                        if info_piece.get_condition == 0:
                            return print("Black")
                        elif info_piece.get_condition == 1:
                            return print("Black_King")
                        elif info_piece.get_condition == 2:
                            return print("Black_Triple_King")

                    elif info_piece.get_color() == "White":
                        if info_piece.get_condition == 0:
                            return print("White")
                        elif info_piece.get_condition == 1:
                            return print("White_King")
                        elif info_piece.get_condition == 2:
                            return print("White_Triple_King")
                else:
                    return None
    def game_winner(self):
        """
        This method will either return the winner of the game or if the game hasn't ended yet, it will indicate so
        """
        for players in self._players:
            if players.get_captured_pieces_count == 12:
                name = players.get_name()
                return print(f"{name}")
            else:
                return print("Game has not ended")


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
        row = [0, 1, 2, 3, 4, 5, 6, 7]
        if piece_color == "Black":
            for i in row[::2]:
                pieces_list.append(Piece(piece_color, (i, 2)))
                pieces_list.append(Piece(piece_color, (i, 0)))
            for i in row[1::2]:
                pieces_list.append(Piece(piece_color, (i, 1)))

        if piece_color == "White":
            for i in row[::2]:
                pieces_list.append(Piece(piece_color, (i, 6)))
            for i in row[1::2]:
                pieces_list.append(Piece(piece_color, (i, 7)))
                pieces_list.append(Piece(piece_color, (i, 5)))

    def piece_captured(self):
        """
        This method adds 1 to the Players captured pieces attribute every time they capture a piece
        """
        self._captured_pieces += 1

    def remove_piece(self, r_piece):
        """
        When the other player jumps over the player's piece, this method removes the piece from their piece list
        """
        piece_list = self._pieces
        for pieces in piece_list:
            if r_piece == pieces:
                piece_list.remove(r_piece)

    def get_pieces_list(self):
        """
        This method will return the pieces list for the given player
        """
        return self._pieces

    def get_name(self):
        """
        This method will return the name parameter for the given Player object
        """
        return self._player_name

    def get_color(self):
        """
        This method will return the color for the given player object
        """
        return self._piece_color

    def get_king_count(self):
        """
        This method will return the number of Kings the player has on the board, it won't count captured kings
        """
        king_count = 0
        for pieces in self._pieces:
            if pieces.get_condition() == 1:
                king_count += 1
        return king_count

    def get_triple_king_count(self):
        """
        This method will return the number of triple Kings the player has on the board, it won't count captured
        triple kings
        """
        trip_king_count = 0
        for pieces in self._pieces:
            if pieces.get_condition == 2:
                trip_king_count += 1
        return trip_king_count

    def get_captured_pieces_count(self):
        """
        This method will return the number of pieces the given player has captured
        """
        return self._captured_pieces
