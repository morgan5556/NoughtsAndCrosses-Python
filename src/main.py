class NoughtsAndCrosses:
    def __init__(self):
        self.playerOne = ""
        self.playerTwo = ""
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.__run_program_loop()

    def __run_program_loop(self):
        print("Welcome to Noughts and Crosses\nMade by Morgan Lyons\n" + "-" * 22)

        while True:
            self.__display_menu()
            user_input = input("Enter a Menu Option: ")

            match user_input:
                case '1':
                    self.__run_player_versus_player()
                case '2':
                    pass
                case '3':
                    print("Thanks for Playing!")
                    break

    def __run_player_versus_player(self):
        self.playerOne = Player("1", "X")
        self.playerTwo = Player("2", "O")

        while True:
            pass

    def __display_menu(self):
        print("Menu\n" + "-" * 22 + "\n1. Player vs Player\n2. Player vs Computer\n3. Quit\n" + "-" * 22)

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

class Player:
    def __init__(self, player_number, symbol): 
        self.score = 0
        self.player_number = player_number
        self.symbol = symbol
        self.name = self.__set_name()

    def __set_name(self):
        self.name = input("Player " + self.player_number + ", please enter your name: ")

if __name__ == '__main__':
	NoughtsAndCrosses()   

    