import unittest
from CheckersGame import Checkers, Player


class MyTestCase(unittest.TestCase):
    def test_1(self):
        board_1 = Checkers()
        board_1.create_player("John", "White")
        board_1.get_players("John").get_color()
        self.assertEqual(board_1.get_players("John").get_color(), "White")

    def test_2(self):
        board_1 = Checkers()
        board_1.create_player("John", "White")
        board_1.create_player("Mary", "Black")
        self.assertIn(board_1.get_players("Mary"), board_1.return_players())

    def test_3(self):
        board_1 = Checkers()
        board_1.create_player("John", "White")
        board_1.create_player("Mary", "Black")
        board_1.play_game("Mary", (5, 2), (4, 3))
        board_1.play_game("John", (2, 1), (3, 2))
        self.assertEqual(board_1.get_checker_details((3, 2)), "White")

    def test_4(self):
        board_1 = Checkers()
        board_1.create_player("John", "White")
        board_1.create_player("Mary", "Black")
        board_1.play_game("Mary", (5, 2), (4, 3))
        board_1.play_game("John", (2, 1), (3, 2))
        board_1.play_game("Mary", (4, 3), (2, 1))
        self.assertEqual(board_1.get_players("Mary").get_captured_pieces_count(), 1)

    def test_5(self):
        board_1 = Checkers()
        board_1.create_player("John", "White")
        board_1.create_player("Mary", "Black")
        board_1.play_game("Mary", (5, 2), (4, 3))
        board_1.play_game("John", (2, 1), (3, 2))
        board_1.play_game("Mary", (4, 3), (2, 1))
        board_1.play_game("John", (1, 0), (3, 2))
        self.assertEqual(board_1.get_players("John").get_captured_pieces_count(), 1)


if __name__ == '__main__':
    unittest.main()