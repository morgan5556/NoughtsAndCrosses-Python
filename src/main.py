class NoughtsAndCrosses:
    def __init__(self):
        self.playerOne = ""
        self.playerTwo = ""
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.turn = 1
        self.__run_program_loop()

    def __run_program_loop(self):
        print("\nWelcome to Noughts and Crosses\nMade by Morgan Lyons\n" + "-" * 22)

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
        self.playerOne = Player("X")
        self.playerOne.set_name(input("Player 1, please enter your name: "))

        self.playerTwo = Player("O")
        self.playerTwo.set_name(input("Player 2, please enter your name: "))

        while True:
            self.__display_board()

            if self.turn == 1:
                self.__add_piece(self.playerOne.get_name(), self.playerOne.get_symbol())
                self.turn += 1
            elif self.turn == 2:
                self.__add_piece(self.playerTwo.get_name(), self.playerTwo.get_symbol())
                self.turn -= 1

    def __display_menu(self):
        print("Menu\n" + "-" * 22 + "\n1. Player vs Player\n2. Player vs Computer\n3. Quit\n" + "-" * 22)

    def __display_board(self):
        print(self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-" * 10)
        print(self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-" * 10)
        print(self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])
        print("-" * 10)

    def __add_piece(self, name, symbol):
        while True:
            position = input(name + " [" + symbol + "], please enter a position: ")
            isValid = self.__check_valid_move(position)

            if isValid == True:
                if position == "1":
                    self.board[0][0] = symbol
                elif position == "2":
                    self.board[0][1] = symbol
                elif position == "3":
                    self.board[0][2] = symbol
                elif position == "4":
                    self.board[1][0] = symbol
                elif position == "5":
                    self.board[1][1] = symbol
                elif position == "6":
                    self.board[1][2] = symbol
                elif position == "7":
                    self.board[2][0] = symbol
                elif position == "8":
                    self.board[2][1] = symbol
                elif position == "9":
                    self.board[2][2] = symbol
                break
            else:
                print("Not a valid move!")

    def __check_valid_move(self, position):
        match position:
            case '1':
                current_state = self.board[0][0]
            case '2':
                current_state = self.board[0][1]
            case '3':
                current_state = self.board[0][2]
            case '4':
                current_state = self.board[1][0]
            case '5':
                current_state = self.board[1][1]
            case '6':
                current_state = self.board[1][2]
            case '7':
                current_state = self.board[2][0]
            case '8':
                current_state = self.board[2][1]
            case '9':
                current_state = self.board[2][2]
                
        if current_state == "X" or current_state == "O":
            return False
        else:
            return True

    def __check_for_win(self):
        pass

class Player:
    def __init__(self, symbol): 
        self.score = 0
        self.symbol = symbol
        self.name = ""

    #-------------------- getters and setters --------------------
    def get_score(self):
        return self.score

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

if __name__ == '__main__':
	NoughtsAndCrosses()   

    