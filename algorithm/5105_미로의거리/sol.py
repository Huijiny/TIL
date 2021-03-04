import sys
import pandas
sys.stdin = open("sample_input (1).txt")
def is_safe(y, x):
    if 0 <= x < N and 0 <= y < N and miro[y][x] != 1:
        return True
    return False

def bfs(col, row):
    dcol = [-1, 1, 0, 0]
    drow = [0, 0, -1, 1]
    queue = []
    queue.append((col, row))
    count = 0
    path = []
    while queue:
        go = queue.pop(0)
        path.append(go)
        count += 1
        visited[go[0]][go[1]] = True
        if miro[go[0]][go[1]] == 3:
            return distance[go[0]][go[1]] -1
        for i in range(4):
            new_col = dcol[i] + go[0]
            new_row = drow[i] + go[1]
            if is_safe(new_col, new_row) and not visited[new_col][new_row]:
                distance[new_col][new_row] = distance[go[0]][go[1]] + 1
                queue.append((new_col, new_row))
    return 0
T = int(input())
for tc in range(1, T+1):
    start = ()
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    for col in range(N):
        for row in range(N):
            if miro[col][row] == 2:
                start = (col, row)
            if miro[col][row] == 1:
                visited[col][row] = True
    distance = [[0] * N for _ in range(N)]
    print("#{} {}".format(tc,bfs(start[0], start[1])))