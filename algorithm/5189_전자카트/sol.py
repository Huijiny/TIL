import sys
sys.stdin = open("sample_input (3).txt")


def search(row, sum_):
    global min_sum, visited
    # visited 0 빼고 다 True이면,
    if all(visited[1:]):
        sum_ += cost[row][0]
        if min_sum > sum_:
            min_sum = sum_
        return
    else:
        for i in range(1, N):
            if not visited[i]:
                if i == row:
                    continue
                sum_ += cost[row][i]
                visited[i] = True
                search(i, sum_)
                visited[i] = False
                sum_ -= cost[row][i]

T = int(input())
for tc in range(1, T+1):
    min_sum = 9999999
    N = int(input())
    visited = [False] * N
    cost = [list(map(int, input().split())) for _ in range(N)]
    search(0, 0)
    print("#{} {}".format(tc, min_sum))