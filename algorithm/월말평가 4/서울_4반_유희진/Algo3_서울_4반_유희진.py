# kruscal을 위한 find함수
def find(x):
    if p[x] == x:
        return x
    return find(p[x])

# kruscal을 위한 union함수
def union(x, y):
    x = find(x)
    y = find(y)
    p[y] = x

# kruscal 알고리즘
def plan_A(weights):
    total = 0
    for a, b, w in weights:
        # 두 지점이 한 부모안에 없다면
        if find(a) != find(b):
            # 합쳐주고
            union(a, b)
            # 비용 추가해주기
            total += w
    return total

# 다익스트라 알고리즘
def plan_B(start):
    INF = float('inf')
    # 거리 비용, 방문여부 변수 선언
    distance = [INF for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]
    distance[start] = 0
    # V번 반복할것.
    for _ in range(V):
        cur_node = 1
        min_distance = INF
        # 1부터 시작함.
        # 가장 작은 지점 찾기
        for n in range(1, V+1):
            if not visited[n] and distance[n] < min_distance:
                min_distance = distance[n]
                cur_node = n
        # 지점 방문체크
        visited[cur_node] = True
        # 그 지점에서 인접한 노드 중에서
        for weight, node in adj[cur_node]:
            next_weight = distance[cur_node] + weight
            # 다음 노드 방문 아직 안했고, 거리가 방금 지나온 노드 + 현재 노드 웨이트보다 크면 거리 비용 갱신해줘.
            if not visited[node] and distance[node] > next_weight:
                distance[node] = next_weight
    # V번의 거리비용 리턴
    return distance[V]

T = int(input())
for tc in range(1, T+1):
    V, E, M = map(int, input().split())
    p = [i for i in range(V + 1)]
    weights = [list(map(int, input().split())) for _ in range(E)]
    # 다익스트라에 쓰일 인접노드 저장
    adj = [[] for _ in range(V + 1)]
    for a, b, w in weights:
        adj[a].append((w, b))
    # 크루스칼 알고리즘에 쓰일 거리 기준으로 소팅
    weights.sort(key=lambda x:x[2])

    # 플랜A 실행
    budget = plan_A(weights)
    # M 이하일 경우 성공
    if budget <= M:
        budget = M - budget
    # 아닐경우 플랜 B 실행
    else:
        budget = plan_B(1)
        # M이하일 경우 성공
        if budget <= M:
            budget = M - budget
        # 아닐경우 -1 반환        else:
            budget = -1
    print("#{} {}".format(tc, budget))