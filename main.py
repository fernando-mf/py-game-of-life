import random
import os
import time

DIMENSION = 30

OUTER_DIMENSION = DIMENSION + 2

SEPARATOR = ' '
CELL_CHAR = '@'
EMPTY_CHAR = ' '

FRAMERATE = 25
ITERATIONS = 500
RANDOM_PERCENTAGE = 40
MAX_RAND = 10000000000000000000000000

def clear():
    os.system('clear')

def getRandomCell():
    percent = MAX_RAND * (RANDOM_PERCENTAGE / 100.0)
    rand = random.randint(0, MAX_RAND)

    return True if rand < percent else False

def isOutsideAxis(point):
    return point == 0 or point == DIMENSION + 1

def initBoard():
    board = [[getRandomCell() for x in range(OUTER_DIMENSION)] for y in range(OUTER_DIMENSION)]

    for x in range(OUTER_DIMENSION):
        for y in range(OUTER_DIMENSION):
            isOutsideX = isOutsideAxis(x)
            isOutsideY = isOutsideAxis(y)

            if isOutsideX or isOutsideY:
                board[x][y] = False
    
    return board

def renderBoard(board):
    for x in range(OUTER_DIMENSION):
        row = range(OUTER_DIMENSION)

        for y in range(OUTER_DIMENSION):
            row[y] = EMPTY_CHAR if board[x][y] is False else CELL_CHAR
        
        # We display an empty row for `out of the grid` indexes
        rowString = SEPARATOR.join(row) if not isOutsideAxis(x) else ''
        print(rowString)


def getNeighbourCount(cellX, cellY, board):
    neighbourCount = 0

    for x in range(cellX - 1, cellX + 2):
        for y in range(cellY - 1, cellY + 2):

            if (x, y) == (cellX, cellY):
                continue
                
            if board[x][y] is True:
                neighbourCount += 1
    
    return neighbourCount


def applyRules(board):
    nextBoard = initBoard()

    for x in range(1, OUTER_DIMENSION - 1):
        for y in range(1, OUTER_DIMENSION - 1):
            neighbourCount = getNeighbourCount(x, y, board)
            cell = board[x][y]
            nextCell = False
            
            if cell and neighbourCount < 2 or neighbourCount > 3:
                nextCell = False
            elif cell and neighbourCount >= 2 and neighbourCount <= 3:
                nextCell = True
            elif not cell and neighbourCount is 3:
                nextCell = True

            nextBoard[x][y] = nextCell

    return nextBoard


def main():
    board = initBoard()

    i = 0
    while(i < ITERATIONS):
        clear()
        renderBoard(board)
        board = applyRules(board)
        time.sleep(1.0 / FRAMERATE)
        i += 1


if __name__ == "__main__":
    main()