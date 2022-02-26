import random
def minimax(position,depth,maximizer):
    tic_tac_toe2.update_board(position)
    if tic_tac_toe2.is_player_win("X"):
        return [1]
    elif tic_tac_toe2.is_player_win("O"):
        return [-1]
    elif depth == 0:
        return [0]
    elif tic_tac_toe2.is_board_filled():
        return [0]
    if maximizer:
        vmax=-2
        for i in range(len(tic_tac_toe2.board)):
            for j in range(len(tic_tac_toe2.board[0])):
                if tic_tac_toe2.board[i][j] == "-":
                    tic_tac_toe2.fix_spot(i,j, "X")
                    value = minimax(tic_tac_toe2.board,depth-1,False)[0]
                    vmax = max(vmax,value)
                    if value >= vmax:
                        move=[i,j]
                    tic_tac_toe2.fix_spot(i,j,"-")
        return [vmax,move[0]+1,move[1]+1]
    else:
        vmin=2
        for i in range(len(tic_tac_toe2.board)):
            for j in range(len(tic_tac_toe2.board[0])):
                if tic_tac_toe2.board[i][j] == "-":
                    tic_tac_toe2.fix_spot(i,j,"O")
                    value = minimax(tic_tac_toe2.board,depth-1,True)[0]
                    vmin = min(vmin,value)
                    if value <= vmin:
                        move=[i,j]
                    tic_tac_toe2.fix_spot(i,j,"-")
        return [vmin,move[0]+1,move[1]+1]


class TicTacToe:

    def __init__(self):
        self.board = []

    def update_board(self,position):
        self.board = position
    
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            if self.board[row-1][col-1]=="-":
                self.fix_spot(row - 1, col - 1, player)
            else:
                print("Hatali kare !")
                break

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)
            
            if player == "X":
                move = minimax(self.board,9,True)
                self.fix_spot(move[1]-1, move[2]-1, player)
                # checking whether current player is won or not
                if self.is_player_win(player):
                    print(f"Player {player} wins the game!")
                    break

                # checking whether the game is draw or not
                if self.is_board_filled():
                    print("Match Draw!")
                    break

                player = self.swap_player_turn(player)

            else:
                move = minimax(self.board,9,False)
                self.fix_spot(move[1]-1, move[2]-1, player)
                # checking whether current player is won or not
                if self.is_player_win(player):
                    print(f"Player {player} wins the game!")
                    break

                # checking whether the game is draw or not
                if self.is_board_filled():
                    print("Match Draw!")
                    break
                player = self.swap_player_turn(player)
                


        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe2 = TicTacToe()
tic_tac_toe.start()
