#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    res = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    """Initialize the board"""
    for i in range(n):
        res.append([i, None])

    def queen_exists(pos):
        """Checks if a queen exists at pos
        Return:
            True: if queen exists
            False: if not
        """
        for i in range(n):
            if pos == res[i][1]:
                return True
        return False

    def is_valid(x, y):
        """
        Determines whether the position on the
        chess board is valid for placement
        """
        if (queen_exists(y)):
            return False
        i = 0
        while (i < x):
            if abs(res[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def reset_board(i):
        """Reset the chess board"""
        for y in range(i, n):
            res[y][1] = None

    def backtrack(y):
        """Recursive backtracking to find all solutions"""
        for i in range(n):
            reset_board(y)
            if is_valid(y, i):
                res[y][1] = i
                if (y == n - 1):
                    print(res)
                else:
                    backtrack(y + 1)

    backtrack(0)
