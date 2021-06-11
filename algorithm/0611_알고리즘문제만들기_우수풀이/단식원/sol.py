import sys
sys.stdin = open("sample_input (5).txt")
from pprint import pprint
T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]

    def bfs():
        pass


    def rec(x, y, idx):
        if idx == 3:
            for i in range(n):
                for j in range(m):
                    print(room[i][j], end=' ')
                print()
            print()
        else:
            if 0 <= x < m and 0 <= y < n:
                if room[y][x] == 0:
                    room[y][x] = 3
                    rec(x, y+1, idx+1)
                    rec(x+1, y, idx+1)
                    rec(x+1, y+1, idx+1)
                    room[y][x] = 0
    for i in range(n):
        for j in range(m):
            rec(n, m, 0)