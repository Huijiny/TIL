import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    answer = 0
    start = 0
    end = 0
    miro = [input().split() for _ in range(N)]
    way = []
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start = (i, j)
            if miro[i][j] == 3:
                end = (i, j)
    dcol = [1, -1, 0, 0]
    drow = [0, 0, 1, -1]
    c_col = start[0]
    c_row = start[1]
    while current != 3:
        current = miro[c_col][c_row]
        if current == 3:
            answer = 1
            break
        for i in range(4):
            new_col = 
