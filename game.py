def printBoard(board):
    print()
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print()

def check_win(board, player):
    win_cond = [player] * 3
    # Check rows and columns
    for i in range(3):
        if board[i] == win_cond or [board[j][i] for j in range(3)] == win_cond:
            return True
    # Check diagonals
    if [board[i][i] for i in range(3)] == win_cond or [board[i][2-i] for i in range(3)] == win_cond:
        return True
    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    cell_mapping = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}

    while True:
        printBoard(board)
        player = players[turn]
        print(f"Player {player}'s turn")

        # Get valid move
        while True:
            try:
                move = int(input("Enter a number between 1 and 9: "))
                if move in cell_mapping:
                    row, col = cell_mapping[move]
                    if board[row][col] == ' ':
                        board[row][col] = player
                        break
                    else:
                        print("Cell already taken, try again.")
                else:
                    print("Invalid input, please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input, please enter a number.")

        if check_win(board, player):
            printBoard(board)
            print(f"Player {player} wins!")
            break

        if check_draw(board):
            printBoard(board)
            print("It's a draw!")
            break

        turn = 1 - turn

if __name__ == "__main__":
    main()
