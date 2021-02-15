import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dc = [1,-1,0,0]
    dr = [0,0,1,-1]
    result = 0
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    for col in range(N):
        for row in range(N):
            center = matrix[col][row]
            for i in range(4):
                new_col = col+dc[i]
                new_row = row+dr[i]
                if new_col >= N or new_col < 0 or new_row >= N or new_row < 0:
                    continue
                else:
                    value = center-matrix[new_col][new_row]
                    if value < 0:
                        value *= -1
                    result += value


    print("#{} {}".format(tc, result))
