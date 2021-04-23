import sys
sys.stdin = open('input (5).txt')

def get_distance(now, next):
    return abs(now[0] - next[0]) ** 2 + abs(now[1] - next[1]) ** 2


def prim(start_node, V):
    global matrix

    INF = float('inf')
    parents = [None] * N
    cost = [INF] * N
    cost[start_node] = 0

    visited = [False for _ in range(V)]

    for _ in range(V):
        minimum_cost = INF
        for node in range(V): # 0, 1, 2, 3
            if not visited[node] and cost[node] < minimum_cost: # 아직 방문안하고, 비용이 젤 낮은 애. 가까운 애.
                next_node = node # 젤 가까운 코스트를 가진 애로 가.
                minimum_cost = cost[node] # 젤 적은 코스트 갱신해.
        visited[next_node] = True # 방문

        adj_nodes = matrix[next_node] # 다음 노드의 인접한 애들을 뽑아.
        for adj_node in range(len(adj_nodes)): # 모든 인접한 노드들에 대하여
            weight = adj_nodes[adj_node] # 비용 뽑고,
            if not visited[adj_node] and weight < cost[adj_node]: # 방문안했고, 비용이 현재 비용보다 작으면
                cost[adj_node] = weight # 비용 갱신해주고
                parents[adj_node] = next_node # 부모도 얘로 갱신해줘.

    return sum(cost)


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

    total = prim(0, N)
    tax = round(total, 2)
    print("#{} {}".format(tc, tax))