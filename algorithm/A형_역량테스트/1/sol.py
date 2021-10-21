import sys
sys.stdin = open("sample_input (5).txt")
from pprint import pprint

def bfs(col, row, people):
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    tmp[col][row] = 0
    cur_sec = 0
    secs = []
    q = [(col, row, 0)]
    visited = [(col, row)]
    dcol = [1, -1, 0, 0]
    drow = [0, 0, 1, -1]

    while len(q):
        ccol, crow, csec = q[0]
        q = q[1:]

        if (ccol, crow) in people:
            if cur_sec == csec:
                cur_sec += 1
            else:
                cur_sec = max(cur_sec, csec) + 1
            secs.append((ccol, crow, cur_sec))

        for i in range(4):
            ncol = ccol + dcol[i]
            nrow = crow + drow[i]
            if 0 <= ncol < n and 0 <= nrow < n and (ncol, nrow) not in visited:
                q.append((ncol, nrow, csec+1))
                visited.append((ncol, nrow))
                tmp[ncol][nrow] = csec+1
    pprint(tmp)
    return secs

T = int(input())
for tc in range(1, T+1):
    result = 0
    n = int(input())

    maps = [list(map(int, input().split(" "))) for _ in range(n)]
    exits = []
    people = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1:
                people.append((i, j))
            if maps[i][j] == 2:
                exits.append((i, j))

    secs = []
    for exit in exits:
        col, row = exit
        sec = bfs(col, row, people)
        secs.append(sec)

    e1 = secs[0]
    e2 = secs[1]
    print(e1)
    print(e2)

    for p in people:
        s1 = 0
        s2 = 0
        col, row = p
        for e in e1:
            c, r, s = e
            if col == c and row == r:
                s1 = s
        for e in e2:
            c, r, s = e
            if col == c and row == r:
                s2 = s
        print(s1, s2)
        print("둘중에 작은",min(s1, s2))
        result = max(result, min(s1, s2))


    print("#{} {}".format(tc, result))