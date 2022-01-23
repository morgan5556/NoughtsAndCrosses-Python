import random

class NoughtsAndCrosses:
    def __init__(self):

        ''' 
        This method declares all the variables that are needed for the game to 
        run. From this, the program loop is executed.
        '''

        self.playerOne = ""
        self.playerTwo = ""
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.turn = 1
        self.plays = 0
        self.__run_program_loop()

    def __run_program_loop(self):

        '''
        This method runs the main program loop based off the user's selections
        for the menu. Different methods are executed depending on the user input.
        '''

        print("\nWelcome to Noughts and Crosses\nMade by Morgan Lyons\n" + "-" * 22)

        while True:
            self.__display_menu()
            user_input = input("Enter a Menu Option: ")
            print("-" * 22)

            match user_input:
                case '1':
                    self.__run_player_versus_player()
                case '2':
                    self.__run_player_vs_computer()
                case '3':
                    pass
                case '4':
                    print("Thanks for Playing!")
                    break

    def __run_player_versus_player(self):

        '''
        This method runs the game loop for the player vs player mode. It 
        instantiantes new players and has a main loop that allows the game
        to run in an efficient way.
        '''

        self.playerOne = Player("X")
        self.playerOne.set_name(input("Player 1, please enter your name: "))

        self.playerTwo = Player("O")
        self.playerTwo.set_name(input("Player 2, please enter your name: "))

        while True:
            self.__display_board()

            if self.turn == 1:
                self.__add_piece(self.playerOne.get_name(), self.playerOne.get_symbol())
                winner = self.__check_for_win(self.playerOne.get_symbol())

                if winner == True:
                    self.__display_board()
                    print(self.playerOne.get_name() + " has won the game!\n\n")
                    break

                self.turn += 1

            elif self.turn == 2:
                self.__add_piece(self.playerTwo.get_name(), self.playerTwo.get_symbol())
                winner = self.__check_for_win(self.playerTwo.get_symbol())

                if winner == True:
                    self.__display_board()
                    print(self.playerTwo.get_name() + " has won the game!\n\n")
                    break

                self.turn -= 1

            if winner == "Draw":
                self.__display_board()
                print("The game has resulted in a draw!\n\n")
                break

        self.__reset_game()

    def __run_player_vs_computer(self):
        player_select = input("Please select X or O: ")

        match player_select:
                case 'X':
                    self.playerOne = Player("X")
                    self.playerOne.set_name(input("Player 1, please enter your name: "))

                    self.playerTwo = Player("O")
                    self.playerTwo.set_name("COMPUTER")
                    self.playerTwo.set_computer(True)

                case 'O':
                    self.playerOne = Player("X")
                    self.playerOne.set_name("COMPUTER")
                    self.playerOne.set_computer(True)

                    self.playerTwo = Player("O")
                    self.playerTwo.set_name(input("Player 2, please enter your name: "))

        while True:
            if self.turn == 1:
                isComputer = self.playerOne.get_computer()

                if isComputer == True:
                    self.__computer_adds_piece(self.playerOne.get_symbol())
                elif isComputer == False:
                    self.__display_board()
                    self.__add_piece(self.playerOne.get_name(), self.playerOne.get_symbol())

                winner = self.__check_for_win(self.playerOne.get_symbol())

                if winner == True:
                    self.__display_board()
                    print(self.playerOne.get_name() + " has won the game!\n\n")
                    break

                self.turn += 1

            elif self.turn == 2:
                isComputer = self.playerTwo.get_computer()

                if isComputer == True:
                    self.__computer_adds_piece(self.playerTwo.get_symbol())
                elif isComputer == False:
                    self.__display_board()
                    self.__add_piece(self.playerTwo.get_name(), self.playerTwo.get_symbol())

                winner = self.__check_for_win(self.playerTwo.get_symbol())

                if winner == True:
                    self.__display_board()
                    print(self.playerTwo.get_name() + " has won the game!\n\n")
                    break

                self.turn -= 1

            if winner == "Draw":
                self.__display_board()
                print("The game has resulted in a draw!\n\n")
                break

        self.__reset_game()

    def __display_menu(self):

        '''
        This method displays the menu to the user.
        '''

        print("Menu\n" + "-" * 22 + "\n1. Player vs Player\n2. Player vs Computer [Easy]\n3. Player vs Computer [Impossible]\n4. Quit\n" + "-" * 22)

    def __display_board(self):

        '''
        This method displays the game board to the user.
        '''

        print("\n\n" + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-" * 10)
        print(self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-" * 10)
        print(self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])
        print("-" * 10)

    def __add_piece(self, name, symbol):

        '''
        This method adds pieces to the board, by first checking if it is a
        valid move through another method.
        '''

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
                self.plays += 1
                break
            else:
                print("Not a valid move!")

    def __computer_adds_piece(self, symbol):
            while True:
                position = str(random.randint(1, 9))
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
                    self.plays += 1
                    break

    def __check_valid_move(self, position):

        '''
        This method checks to see if the move chosen by the user is valid.
        '''

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

    def __check_for_win(self, symbol):

        '''
        This method checks to see if the user that has just played has won.
        It checks for horizontal wins, then vertical wins, then diagonal wins,
        then finally checks for a draw if 9 "plays" have occured.
        '''

        # checks for horizontal wins
        if self.board[0] == [symbol, symbol, symbol]:
            return True
        elif self.board[1] == [symbol, symbol, symbol]:
            return True
        elif self.board[2] == [symbol, symbol, symbol]:
            return True

        # checks for vertical wins
        if self.board[0][0] == symbol and self.board[1][0] == symbol and self.board[2][0] == symbol:
            return True
        elif self.board[0][1] == symbol and self.board[1][1] == symbol and self.board[2][1] == symbol:
            return True
        elif self.board[0][2] == symbol and self.board[1][2] == symbol and self.board[2][2] == symbol:
            return True
        
        # checks for diagonal wins
        if self.board[0][0] == symbol and self.board[1][1] == symbol and self.board[2][2] == symbol:
            return True
        elif self.board[0][2] == symbol and self.board[1][1] == symbol and self.board[2][0] == symbol:
            return True

        # checks for draw
        if self.plays == 9:
            return "Draw"

        return False

    def __reset_game(self):

        '''
        This resets all the variables in the game class to their original
        state for the game to restart.
        '''

        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.turn = 1
        self.plays = 0

class Player:
    def __init__(self, symbol): 

        ''' 
        This method declares all the variables that are needed for the Player
        class.
        '''

        self.symbol = symbol
        self.name = ""
        self.computer = False

    #-------------------- getters and setters --------------------
    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def get_computer(self):
        return self.computer

    def set_name(self, name):
        self.name = name

    def set_computer(self, computer):
        self.computer = computer

if __name__ == '__main__':
	NoughtsAndCrosses()   

    