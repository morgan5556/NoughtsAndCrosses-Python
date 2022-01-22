class NoughtsAndCrosses:
    def __init__(self):
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    def __run_program_loop(self):
        pass

    def __display_menu(self):
        print("Menu\n" + "-" * 22 + "\n1. Player vs Player\n2. Player vs Computer\n" + "-" * 22)

    def __display_board(self):
        print(self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-" * 10)
        print(self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-" * 10)
        print(self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])
        print("-" * 10)

    def __add_piece(self):
        pass

    def __check_for_win(self):
        pass

    def __add_player(self):
        pass

class Player:
    def __init__(self):
        self.name = ""
        self.score = ""
        self.symbol = ""

if __name__ == '__main__':
	NoughtsAndCrosses()   

    