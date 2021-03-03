import sys
sys.stdin = open("dfs_bfs_input.txt")

def bfs(adj, v):
    visited = [0] * (N+1)
    queue = []
    queue.append(v)
    path = []
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            path.append(t)
            queue += sorted(adj[t])
    print(path)

T = int(input())
for tc in range(1, T+1):
    N, M, V = map(int, input().split())
    adj = [[] for _ in range(N+1)]

    for _ in range(M):
        start, end = map(int, input().split())
        adj[start].append(end)
        adj[end].append(start)
    for i in range(N):
        if len(adj[i]) > 1:
            sorted(adj[i])
    bfs(adj, V)
    print()

    # 뒤에 있을수록 마지막 방문한 v 인접점
    # 앞에있을수록 최초 v에 인접함.
    # dfs는 마지막 방문한 곳에서 인접한 곳을 찾아나가는 것이고, bfs는 먼저 인접해있는 순서대로 다 보겠다는 뜻임.