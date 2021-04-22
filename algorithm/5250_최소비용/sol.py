import sys
sys.stdin = open('sample_input (5).txt')

def bfs(y, x):
    q = [(y, x)]

    while q:
        # 현재 좌표 꺼내서
        cur_y, cur_x = q.pop(0)
        # 4방향 탐색하면서
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            # 범위 내에 있다면
            if 0 <= new_x < N and 0 <= new_y < N:
                weight = 1
                # 원래 있던 곳에서 새로운 곳이 더 크다면? 단차 더해줘.
                if area[new_y][new_x] > area[cur_y][cur_x]:
                    weight += area[new_y][new_x] - area[cur_y][cur_x] # 단차
                # 이전 연료에 갈 때 들어가는 연료 1 더해줌.
                if distance[new_y][new_x] > distance[cur_y][cur_x] + weight:
                    distance[new_y][new_x] = distance[cur_y][cur_x] + weight
                    q.append((new_y, new_x))

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = int(1e9)
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF for _ in range(N)] for _ in range(N)]
    distance[0][0] = 0
    bfs(0, 0)
    print("#{} {}".format(tc, distance[N-1][N-1]))