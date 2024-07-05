from Board import Board
from Player import Player
import numpy as np


def utility1(board: Board, player: Player, opponent: Player):
    value = 0
    if player.terminal_test():
        value += 1000000

    value += board.shortestPath(opponent) - board.shortestPath(player) * 1.3

    return value


def utility2(board: Board, player: Player, opponent: Player):
    value = 0
    if player.terminal_test():
        value += 1000000

    value += board.shortestPath(opponent) - board.shortestPath(player) * 1.1

    return value
