import heapq

def change_adj(trap_num, adj):
    for i in range(len(adj)):
        if adj[trap_num][i]:
            adj[trap_num][i], adj[i][trap_num] = adj[i][trap_num], adj[trap_num][i]
    for i in range(len(adj)):
        if adj[i][trap_num]:
            adj[trap_num][i], adj[i][trap_num] = adj[i][trap_num], adj[trap_num][i]
    return adj

def dijstra(start, distance, adj, traps):
    q = []
    distance[start] = 0

    heapq.heappush(q, (0, start))

    while q:
        w, node = heapq.heappop(q)
        print(node)
        if node in traps:
            adj = change_adj(node, adj)

        for end_node in range(len(adj[node])):
            weight = adj[node][end_node]
            if weight == 0:
                continue

            next_weight = weight + distance[node]
            if distance[end_node] > next_weight:
                distance[end_node] = next_weight
                heapq.heappush(q, (next_weight, end_node))
            print(q)
    return distance

def solution(n, start, end, roads, traps):
    INF = float('inf')
    distance = [INF for _ in range(n+1)]
    adj = [[0] * (n+1) for _ in range(n+1)]

    for road in roads:
        adj[road[0]][road[1]] = road[2]
    print(adj)
    distance = dijstra(start, distance, adj, traps)

    answer = distance[end]
    print(answer)
    print(distance)
    return answer

solution(4, 1, 4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])