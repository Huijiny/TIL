import sys
sys.stdin = open("sample_input (3).txt")


def minimum_cost(product, cost):
    global min_cost
    if product == N:
        if min_cost > cost:
            min_cost = cost

    if min_cost < cost:
        return

    else:
        # 공장을 돌면서 공장이 visited되지 않은 애
        for i in range(N):
            if not visited[i]:
                # 공장 visited되고,
                visited[i] = True
                # 다음 프로덕트 만들러감.비용은 현재 공장에서 현재 프로덕트 만드는 비용으로.
                minimum_cost(product + 1, cost + factories[product][i])
                # 공장 visited 원복
                visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    factories = [list(map(int, input().split())) for _ in range(N)]
    # 공장 방문 여부
    visited = [False] * N
    min_cost = 999999
    cost = 0
    minimum_cost(0, 0)
    print("#{} {}".format(tc, min_cost))