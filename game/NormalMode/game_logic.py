class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_turn = player1
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def make_move(self, player, row, col):
        if self.board[row][col] == '' and player == self.current_turn:
            self.board[row][col] = 'X' if player == self.player1 else 'O'
            if self.check_winner(row, col):
                self.winner = player
            else:
                self.current_turn = self.player2 if self.current_turn == self.player1 else self.player1
            return True
        return False

    def check_winner(self, row, col):
        # Check row
        if all(self.board[row][i] == self.board[row][col] for i in range(3)):
            return True
        # Check column
        if all(self.board[i][col] == self.board[row][col] for i in range(3)):
            return True
        # Check diagonals
        if row == col and all(self.board[i][i] == self.board[row][col] for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i][2 - i] == self.board[row][col] for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(self.board[row][col] != '' for row in range(3) for col in range(3))

    def get_board(self):
        return self.board

    def get_current_turn(self):
        return self.current_turn

    def get_winner(self):
        return self.winner


"""_Example usage_

if __name__ == "__main__":
    game = TicTacToe("player1", "player2")
    game.make_move("player1", 0, 0)
    game.make_move("player2", 1, 0)
    ...
    game.make_move("player1", 1, 1)
    game.make_move("player2", 2, 0)
    game.make_move("player1", 2, 2)

    winner = game.get_winner()
    print(f"The winner is: {winner}")       # => The winner is: player1
"""
