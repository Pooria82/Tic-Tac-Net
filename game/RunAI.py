from Player import Player
from Board import Board
from Action import Action, doAction
player1 = Player("P1")
player2 = Player("P2")
board = Board()
player1.doSet(1,1,board)
player2.doSet(2,1,board)
player2.doSet(0,0,board)
player2.doSet(1,0,board)
player2.doSet(2,0,board)
print(player2.terminal_test(board))

board.displayBoard()


