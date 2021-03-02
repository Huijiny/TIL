import sys
sys.stdin = open("sample_input(1).txt")
def swiper(row, col, color):
    matrix[col][row] = color

    for dcol in [-1, 0, 1]:
        for drow in [-1, 0, 1]:
            if dcol == drow == 0:
                continue

            new_col = col + dcol
            new_row = row + drow
            check = False

            while 0 <= new_row < N and 0 <= new_col < N:
                if matrix[new_col][new_row] == 3 - color:
                    new_col += dcol
                    new_row += drow
                elif matrix[new_col][new_row] == color:
                    check = True
                    break
                else:
                    break

            if check:
                origin_row = row+drow
                origin_col = col+dcol
                while origin_row != new_row or origin_col != new_col:
                    matrix[origin_col][origin_row] = color
                    origin_row += drow
                    origin_col += dcol

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = [[0] * N for _ in range(N)]
    mid_idx = N // 2 - 1
    matrix[mid_idx][mid_idx] = matrix[mid_idx+1][mid_idx+1] = 2
    matrix[mid_idx][mid_idx+1] = matrix[mid_idx+1][mid_idx] = 1


    for _ in range(M):
        row, col, color = list(map(int,input().split()))
        swiper(row-1, col-1, color)

    black = white = 0
    for col in range(N):
        for row in range(N):
            if matrix[col][row] == 1:
                black += 1
            elif matrix[col][row] == 2:
                white += 1

    print("#{} {} {}".format(tc, black, white))