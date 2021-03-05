import sys
sys.stdin = open("sample_input (1).txt")
# Q(to_visits)에 넣는 순간 방문 완료로 판
def bfs(G, start):
    visited = [0] * (V + 1)
    distance = [0] * (V + 1)
    queue = [start]
    visited[start] = True
    while queue:
        t = queue.pop(0)
        for i in G[t]:
            if not visited[i]:
                # i는 이미 방문 완료로 판별 & 거리 측정.
                queue.append(i)
                visited[i] = True
                distance[i] = distance[t] + 1
                if i == goal:
                    return distance[i]
    return 0
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())


    matrix = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        matrix[start].append(end)
        matrix[end].append(start)
    S, goal = map(int, input().split())
    print("#{} {}".format(tc, bfs(matrix, S)))