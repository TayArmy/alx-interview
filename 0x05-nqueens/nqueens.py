#!/usr/bin/python3
""" Solving the nqueens problem where n queens are placed in such
    a way that one queen cannot attack the other...
"""
import sys


def isValid(cBoard, row, col):
    """ checks if a possible solution is valid, returning
        true or false 
    """
    for i in range(row):
        if cBoard[i] == col or \
           cBoard[i] - i == col - row or \
           cBoard[i] + i == col + row:
            return False
    return True

def backTrack(cBoard, row):
    """ backtrack to find valid solutions from the board set """
    # if row == len(cBoard):
    #     print(str(cBoard).replace(", ", ","))
    #     return
    # for col in range(len(cBoard)):
    #     if isValid(cBoard, row, col):
    #         cBoard[row] = col
    #         backTrack(cBoard, row + 1)

    # set base case
    if row == len(cBoard):
        print([[i, cBoard[i]] for i in range(len(cBoard))])
        return
    for col in range(len(cBoard)):
        if isValid(cBoard, row, col):
            cBoard[row] = col
            backTrack(cBoard, row + 1)


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print('Usage: nqueens N')
            sys.exit(1)
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    # initialize a square chess board row (solution set)
    cBoard = [-1] * n
    backTrack(cBoard, 0)