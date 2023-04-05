# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 3/19/2023
# Description: Class called "Checkers" that shows a checkers board and lets two players
#              play a game of checkers. Class called "Player" that represents a player
#              in the checkers game.


class Checkers:
    def __init__(self, board=[], players=[]):
        self._board = [[None, "White", None, "White", None, "White", None, "White"],
                       ["White", None, "White", None, "White", None, "White", None],
                       [None, "White", None, "White", None, "White", None, "White"],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       ["Black", None, "Black", None, "Black", None, "Black", None],
                       [None, "Black", None, "Black", None, "Black", None, "Black"],
                       ["Black", None, "Black", None, "Black", None, "Black", None]
                       ]
        self._players = []
        self._turn = "Black"

    def get_turn(self):
        return self._turn

    def create_player(self, player_name, piece_color):
        player = Player(player_name, piece_color)
        self._players.append(player)
        return player

    def play_game(self, player_name, starting_square_location, destination_square_location):
        for player in range(len(self._players)):
            if self._players[player].get_name() == player_name:
                if self._players[player].get_color() == self._turn:
                    if self.get_checker_details(starting_square_location) == self._players[player].get_color():
                        moves = self.possible_moves(starting_square_location)
                        capture_list = self.capture_piece(starting_square_location)

                        if self.get_checker_details(destination_square_location) == None and destination_square_location in moves:
                            self._board[destination_square_location[0]][destination_square_location[1]] = self._turn
                            self._board[starting_square_location[0]][starting_square_location[1]] = None
                            if destination_square_location[0] == 0 and self._turn == 'Black':
                                self._players[player].add_king_count()
                            if destination_square_location[0] == 7 and self._turn == 'White':
                                self._players[player].add_king_count()
                            self.update_turn(player_name)

                        if self.get_checker_details(destination_square_location) == None and destination_square_location in capture_list:
                            self._board[destination_square_location[0]][destination_square_location[1]] = self._turn
                            m_list = []
                            move_1 = (starting_square_location[0] - 1, starting_square_location[1] + 1)
                            move_2 = (starting_square_location[0] - 1, starting_square_location[1] - 1)
                            move_3 = (starting_square_location[0] + 1, starting_square_location[1] + 1)
                            move_4 = (starting_square_location[0] + 1, starting_square_location[1] - 1)
                            m_list.append(move_1)
                            m_list.append(move_2)
                            m_list.append(move_3)
                            m_list.append(move_4)

                            if destination_square_location[0] == 0 and self._turn == 'Black':
                                self._players[player].add_king_count()
                            if destination_square_location[0] == 7 and self._turn == 'White':
                                self._players[player].add_king_count()

                            for item in m_list:
                                if item not in moves:
                                    if self._board[item[0]][item[1]] != self._turn:
                                        self._board[item[0]][item[1]] = None
                                        self.update_turn(player_name)
                            self._players[player].add_piece_count()
                            self._board[starting_square_location[0]][starting_square_location[1]] = None

    def capture_piece(self, square_location):
        capture_moves = []
        move_5 = (square_location[0] - 2, square_location[1] + 2)
        move_6 = (square_location[0] - 2, square_location[1] - 2)
        move_7 = (square_location[0] + 2, square_location[1] + 2)
        move_8 = (square_location[0] + 2, square_location[1] - 2)

        if self.check_valid(move_5) == True:
            capture_moves.append(move_5)
        if self.check_valid(move_6) == True:
            capture_moves.append(move_6)
        if self.check_valid(move_7) == True:
            capture_moves.append(move_7)
        if self.check_valid(move_8) == True:
            capture_moves.append(move_8)

        return capture_moves



    def possible_moves(self, square_location):
        moves = []
        move_1 = (square_location[0] - 1, square_location[1] + 1)
        move_2 = (square_location[0] - 1, square_location[1] - 1)
        move_3 = (square_location[0] + 1, square_location[1] + 1)
        move_4 = (square_location[0] + 1, square_location[1] - 1)


        if self.check_valid(move_1) == True:
            moves.append(move_1)
        if self.check_valid(move_2) == True:
            moves.append(move_2)
        if self.check_valid(move_3) == True:
            moves.append(move_3)
        if self.check_valid(move_4) == True:
            moves.append(move_4)


        return moves

    def check_valid(self, square_location):
        if self._board[square_location[0]][square_location[1]] == None:
            return True
        else:
            return False

    def update_turn(self, player_name):
        for player in range(len(self._players)):
            if self._players[player].get_name() == player_name:
                if self._players[player].get_color() == "White":
                    self._turn = "Black"
                elif self._players[player].get_color() == "Black":
                    self._turn = "White"

    def get_checker_details(self, square_location):

        return self._board[square_location[0]][square_location[1]]


    def print_board(self):
        # for i in self._board:
        #     print(i)
        print(self._board)

    def get_players(self, name):
        for item in self._players:
            if item.get_name() == name:
                return item

    def return_players(self):
        return self._players

class Player:
    def __init__(self, name, checker_color, piece_count=0, king_count=0, triple_king_count=0):
        self._name = name
        self._checker_color = checker_color
        self._piece_count = piece_count
        self._king_count = king_count
        self._triple_king_count = triple_king_count

    def get_name(self):
        return self._name

    def get_color(self):
        return self._checker_color

    def get_king_count(self):
        return self._king_count
    # def get_triple_king_count(self):

    def add_king_count(self):
        self._king_count += 1

    def add_piece_count(self):
        self._piece_count += 1

    def get_captured_pieces_count(self):
        return self._piece_count

class InvalidSquare(Exception):
    pass

class OutofTurn(Exception):
    pass

class InvalidPlayer(Exception):
    pass


def main():
    b = Checkers()
    b.create_player("John", "White")
    b.create_player("Mary", "Black")
    b.play_game("Mary", (5, 2), (4, 3))
    b.play_game("John", (2, 1), (3, 2))
    b.play_game("Mary", (4, 3), (2, 1))
    b.play_game("John", (1, 0), (3, 2))
    # b.play_game("Mary", (2, 1), (3, 2))
    # b.print_board()
    # print(b.get_players("Mary").get_captured_pieces_count())

    # b.get_checker_details((0, 0))


if __name__ == "__main__":
    main()