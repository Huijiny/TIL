import sys
sys.stdin = open("input (4).txt")

def is_safe(y, x):
    if 0 < y < 16 and 0 < x < 16 and miro[y][x] != 1:
        return True
    return False

def bfs(start):
    visited = [start]
    dcol = [-1, 1, 0, 0]
    drow = [0, 0, -1, 1]
    queue = [start]
    while queue:
        next = queue.pop(0)
        if next == (13, 13):
            return 1
        else:
            for i in range(4):
                new_col = dcol[i] + next[0]
                new_row = drow[i] + next[1]
                if is_safe(new_col, new_row) and not (new_col, new_row) in visited:
                    visited.append((new_col, new_row))
                    queue.append((new_col, new_row))
    return 0
T = 10
for tc in range(1, T+1):
    input()
    n = 16
    miro = [list(map(int, list(input()))) for _ in range(n)]
    print("#{} {}".format(tc,bfs((1,1))))