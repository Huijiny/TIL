import sys
sys.stdin = open("input (2).txt")

T = 10
N = 100
def find_end_point(matrix):
    for i in range(N):
        if matrix[N-1][i] == 2:
            return i

for tc in range(1, T+1):
    case = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    number = 0

    end_point = find_end_point(matrix)

    col = N-1
    row = end_point

    while col != 0:
        if col == N-1: # 99
            col -= 1
        # left row > 1
        if row > 1 and matrix[col][row-1]:
            while row > 1 and matrix[col][row-1]:
                row = row-1
        # right row < 99
        elif row < N-1 and matrix[col][row+1]:
            while row < N-1 and matrix[col][row+1]:
                row = row+1
        col -= 1


    print("#{} {}".format(tc, row))