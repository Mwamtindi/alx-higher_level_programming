#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    for e in range(row):
        if board[e] == col or \
           board[e] - e == col - row or \
           board[e] + e == col + row:
            return False
    return True


def solve(board, row, N):
    if row == N:
        print("[", end="")
        for e in range(N):
            print("[{}, {}]".format(e, board[e]), end="")
            if e != N - 1:
                print(", ", end="")
        print("]")
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve(board, row + 1, N)


def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
