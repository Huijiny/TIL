import sys

sys.stdin = open("input.txt")


def div(col, row, length):
    global count
    if col == r and row == c:
        print(count)
        exit(0)
    if length == 1:
        count += 1
        return

    if not (col <= r < col+length) and not (row <= c < row+length):
        count += length ** 2
        return

    length = length // 2
    div(col, row, length)
    div(col, row + length, length)
    div(col + length, row, length)
    div(col + length, row + length, length)


N, r, c = map(int, input().split())
matrix = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]
count = 0
div(0, 0, 2 ** N)
