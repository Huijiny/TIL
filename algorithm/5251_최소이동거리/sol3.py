import sys
import heapq
sys.stdin = open('sample_input (5).txt')

def dijkstra(start):
    distance[start] = 0
    # 이 노드까지의 웨이트, 노드.
    heapq.heappush(q, (0, start))

    while q:
        w, node = heapq.heappop(q)
        for weight, end_node in adj[node]: # 인접한 점들 중에서
            next_weight = weight + distance[node]
            if distance[end_node] > next_weight:
                distance[end_node] = next_weight
                heapq.heappush(q, (next_weight, end_node))

T = int(input())

for tc in range(1, T+1):
    INF = float('inf')
    N, E = map(int, input().split())
    distance = [INF for _ in range(N + 1)]
    adj = [[] for _ in range(N + 1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((w, e))
    q = []
    dijkstra(0)
    print("#{} {}".format(tc, distance[N]))


def dijkstra1(start):
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        weight, node = heapq.heappop(q)
        for w, next_node in adj[node]:
            next_weight = distance[node] + w
            if distance[next_node] > next_weight:
                distance[next_node] = next_weight
                heapq.heappush(q, (next_weight, next_node))


for tc in  range(1, T+1):
    INF = float('inf')
    N, E = map(int, input().split())
    distance = [INF for _ in range(N + 1)]
    adj = [[] for _ in range(N + 1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((w, e))
    q = []
    dijkstra1(0)
    print("#{} {}".format(tc, distance[N]))