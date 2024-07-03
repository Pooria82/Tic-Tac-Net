from Action import Action
from Board import Board
import typing


class Player:
    def __init__(self, name, isHardMode=False):
        self.name = name
        if name == "P1":
            self.type = "X"
        else:
            self.type = "O"
        self.played_round = 0  # har moqe 3 beshe akharin harekat pak mishe
        self.first_move_cordinate = []
        self.HardMode = isHardMode

    def getValidActions(self, board: Board) -> typing.List[Action]:
        available_actions = []
        return available_actions

    def doSet(self, row, column, board: Board):
        board.setToken(row, column, self.type)
        if self.HardMode:
            if self.played_round < 3:
                self.first_move_cordinate.append((row, column))
            else:
                board.board[self.first_move_cordinate[0][0]][self.first_move_cordinate[0][1]].type = None
                self.first_move_cordinate.append((row, column))
                self.first_move_cordinate.pop(0)
            self.played_round += 1

    def terminal_test(self, board: Board):
        for i in board.getAllDirections():
            if len(i) == 1 and next(iter(i)) == self.type:
                return True
        return False
