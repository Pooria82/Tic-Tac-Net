from tokens import Token


class Board:

    def __init__(self) -> None:

        self.board = [[Token() for _ in range(3)] for _ in range(3)]

    def displayBoard(self):
        for i in self.board:
            for token in i:
                if token.type:
                    print(token.type + " ", end=" ")
                else:
                    print("empty", end=" ")
            print("\n")

    def valid(self, row, col) -> bool:
        """
        Returns true if the given row and col represent a valid location on
        the board.
        """
        return row >= 0 and col >= 0 and row < 3 and col < 3

    def canSetToken(self, row, column) -> bool:
        """
        determines if the cordinates are valid for placing token.
        """
        if self.board[row][column].type == None:
            return True
        else:
            return False

    def setToken(self, row, column, type):
        if self.canSetToken(row, column):
            self.board[row][column].setType(type)

    def getVertical(self):
        result = []
        for i in range(3):
            temp = [x[i].type for x in self.board]
            result.append(set(temp))
        return result

    def getHorizontal(self):
        result = []
        for i in self.board:
            temp = [x.type for x in i]
            result.append(set(temp))
        return result

    def getDiagonal(self):
        result = []
        temp1 = []
        temp2 = []
        for i in range(3):
            temp1.append(self.board[i][i].type)
            temp2.append(self.board[i][2-i].type)

        result.append(set(temp1))
        result.append(set(temp2))
        return result

    def getAllDirections(self):
        result = []
        result.extend(self.getDiagonal())
        result.extend(self.getVertical())
        result.extend(self.getHorizontal())
        return result
