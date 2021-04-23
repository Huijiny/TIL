import sys
sys.stdin = open('input (5).txt')

def get_distance(now, next):
    return abs(now[0] - next[0]) ** 2 + abs(now[1] - next[1]) ** 2


def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])


def union(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    parent = [i for i in range(N)]
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())
    coords = [[xs[i], ys[i]] for i in range(N)]
    matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix[i][j] = get_distance(coords[i], coords[j])

    edge = []
    for i in range(N):
        for j in range(i+1, N):
            w = matrix[i][j]
            edge.append((w, i, j))

    edge.sort()

    total = 0
    for w, i, j in edge:
        if find(i) != find(j):
            union(i, j)
            total += w

    total = total * E
    print("#{} {}".format(tc, round(total)))