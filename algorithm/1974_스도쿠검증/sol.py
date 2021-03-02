import sys
sys.stdin = open("input (4).txt")

T = int(input())
for tc in range(1, T+1):
    point = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
    result = 1
    board = [list(map(int,input().split())) for _ in range(9)]
    for i in range(9):
        total_row = total_col = 0
        for j in range(9):
            total_col += board[i][j] # 세로 우선
            total_row += board[j][i] # 가로 우선
            if (i, j) in point:
                total_square = 0
                for z in range(3):
                    for b in range(3):
                        total_square += board[i+z][j+b]
                if total_square != 45:
                    result = 0
                    break
        if total_col != 45 or total_row != 45:
            result = 0
            break


    print("#{} {}".format(tc,result))