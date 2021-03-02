import sys
sys.stdin = open("sample_input (1).txt")
def is_safe(idx):
    if idx < N and idx >= 0:
        return True
    return False
def dfs(c_col, c_row):
    global result
    if miro[c_col][c_row] == 3:
        result = 1
        return
    visited.append((c_col, c_row))
    for i in range(4):
        new_col = c_col+dcol[i]
        new_row = c_row+drow[i]

        if is_safe(new_row) and is_safe(new_col) and (new_col, new_row) not in visited:
            if miro[new_col][new_row] != 1:
                dfs(new_col, new_row)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start = (i, j)
    dcol = [1, -1, 0, 0]
    drow = [0, 0, 1, -1]
    result = 0
    visited = []
    dfs(start[0], start[1])
    print("#{} {}".format(tc, result))
