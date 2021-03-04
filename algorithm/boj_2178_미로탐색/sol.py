import sys
import pandas as pd
sys.stdin = open("input.txt")


def is_safe(y, x):
    if 0 <= x < M and 0 <= y < N and miro[y][x] != 0:
        return True
    return False


def bfs(col, row):
    # visited 배열 생성
    # queue 배열 생성
    visited = [[0] * M for _ in range(N)]
    queue = [(col, row)]
    while queue:
        p = queue.pop(0)

        if p[0] == N-1 and p[1] == M-1:
            return distance[N-1][M-1]
        dcol = [-1, 1, 0, 0]
        drow = [0, 0, -1, 1]

        for i in range(4):
            new_col = dcol[i] + p[0]
            new_row = drow[i] + p[1]
            if is_safe(new_col, new_row) and not visited[new_col][new_row]:

                visited[new_col][new_row] = 1
                queue.append((new_col, new_row))
                distance[new_col][new_row] = distance[p[0]][p[1]] + 1


N, M = map(int, input().split())
miro = [list(map(int, list(input()))) for _ in range(N)]
distance = [[0] * M for _ in range(N)]
distance[0][0] = 1
print(bfs(0, 0))
