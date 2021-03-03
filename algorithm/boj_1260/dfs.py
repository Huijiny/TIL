import sys
sys.stdin = open("dfs_bfs_input.txt")

def dfs(adj, v):
    visited = [0] * (N+1)
    stack = []
    stack.append(v)
    path = []
    while stack:
        t = stack.pop()
        if not visited[t]:
            visited[t] = True
            path.append(t)
            stack += sorted(adj[t])[::-1]
    print(path)


T = int(input())
for tc in range(1, T+1):
    N, M, V = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    visited = [0] * (N + 1)

    for _ in range(M):
        start, end = map(int, input().split())
        adj[start].append(end)
        adj[end].append(start)
    dfs(adj, V)
    print()