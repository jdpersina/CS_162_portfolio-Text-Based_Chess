# Author: Joseph 'Dan' Persina
# GitHub username: jdpersina
# Date: 3/4/23
# Description: The Checkers game unit tester

import unittest
from CheckersGame import Checkers, Player


class TestCheckersGame(unittest.TestCase):
    """
    This class contains unit tests for the CheckersGame file
    """
    def test_player_creation(self):
        """
        This test shows that the get_name method and get_color method will return the correct string assigned to them
        when a new player is created.
        """
        player_1 = Player("Dan", "Black")
        result_1 = player_1.get_name()
        result_2 = player_1.get_color()
        self.assertEqual(result_1, "Dan")
        self.assertEqual(result_2, "Black")

    def test_piece_population(self):
        """
        Pieces populate automatically when a player is created, and each player starts with 12 pieces. This test will
        demonstrate that when a new player is created, they have 12 pieces assigned to them.
        """
        amount = 0
        player_2 = Player("Darcie", "White")
        for pieces in player_2.get_pieces_list():
            amount += 1
        self.assertTrue(amount == 12)

    def test_piece_color(self):
        """
        Pieces populate to the board automatically when a new player is created. This test is designed to show that when
        a player who chose "White" is created, their list of pieces will not include any black pieces
        """
        player_2 = Player("Mikey", "White")
        for pieces in player_2.get_pieces_list():
            self.assertFalse(pieces.get_color() == "Black")

    def test_population_setup(self):
        """
        The pieces in a game of checkers all start in a specific square in the board. This test will show that the black
        pieces in a game all populate in the correct place. by testing the light squares in the first 3 rows that don't
        ever have pieces on them
        """
        player_1 = Player("Liv", "Black")
        for pieces in player_1.get_pieces_list():
            self.assertFalse((1, 0) == pieces.get_location)
            self.assertFalse((3, 0) == pieces.get_location)
            self.assertFalse((5, 0) == pieces.get_location)
            self.assertFalse((7, 0) == pieces.get_location)
            self.assertFalse((0, 1) == pieces.get_location)
            self.assertFalse((2, 1) == pieces.get_location)
            self.assertFalse((4, 1) == pieces.get_location)
            self.assertFalse((6, 1) == pieces.get_location)
            self.assertFalse((1, 2) == pieces.get_location)
            self.assertFalse((3, 2) == pieces.get_location)
            self.assertFalse((5, 2) == pieces.get_location)
            self.assertFalse((7, 2) == pieces.get_location)

    def test_InvalidSquare(self):
        """
        This test will show the normal pieces move diagonally one space at a time when not taking a piece according
        to the rules
        """
        game = Checkers()
        game.create_player("Alex", "Black")
        game.play_game("Alex", (0, 2), (1, 3))
        piece = game.check_coordinates((1, 3))
        self.assertTrue(piece == "Black")
