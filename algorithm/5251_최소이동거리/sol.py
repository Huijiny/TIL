import sys
import heapq
sys.stdin = open('sample_input (5).txt')
INF = int(1e9)
T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    # 그래프 정보 저장할 변수
    graph = [[] for _ in range(N + 1)]
    # 노드 별 거리 측정 변수
    distance = [INF] * (N + 1)
    for i in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    q = []
    def dijkstra(start):
        distance[start] = 0
        heapq.heappush(q, (0, start))

        # 남은 노드들을 돌면서 1) 아직 방문 안한애
        while q:
            # 가장 작은 노드 선택
            cur_weight, cur_node = heapq.heappop(q)

            # start의 인접점들 중에 방문 안한 모두 heapq에 넣어. 가장 작은게 위로 올 수 있도록.
            for weight, node in graph[cur_node]:
                next_weight = distance[cur_node] + weight
                # 현재 노드에서 weight만큼 가는게 현재 노드까지 갈 수 있는 거리보다 작다면, 현재 노드 갱신해줘.
                if distance[node] > next_weight:
                    distance[node] = next_weight
                    heapq.heappush(q, (next_weight, node))
    dijkstra(0)
    print("#{} {}".format(tc, distance[N]))