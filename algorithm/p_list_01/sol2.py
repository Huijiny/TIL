import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    dc = [1, -1, 0, 0]
    dr = [0, 0, 1, -1]
    result = 0
    matrix = [[0] * (N + 2)]
    for _ in range(N):
        matrix .append([0, *map(int, input().split()), 0])
    matrix.append([[0] * (N + 2)])
    for col in range(1, N+1):
        for row in range(1, N+1):
            for i in range(4):
                center = matrix[col][row]
                new_col = col + dc[i]
                new_row = row + dr[i]
                around = matrix[new_col][new_row]
                if around:
                    value = center - around
                    if value < 0:
                        value *= -1
                    result += value
    print("#{} {}".format(tc, result))