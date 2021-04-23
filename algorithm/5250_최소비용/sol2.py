import sys
sys.stdin = open("sample_input (5).txt")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(x, y):
    q = [(x, y)]
    while q:
        cur_x, cur_y = q.pop(0)

        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                weight = 1
                if area[new_x][new_y] > area[cur_x][cur_y]:
                    weight += area[new_x][new_y] - area[cur_x][cur_y]
                if distance[new_x][new_y] > distance[cur_x][cur_y] + weight:
                    distance[new_x][new_y] = distance[cur_x][cur_y] + weight
                    q.append((new_x, new_y))
T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = int(1e9)
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF for _ in range(N)] for _ in range(N)]
    distance[0][0] = 0
    dijkstra(0, 0)
    print("#{} {}".format(tc, distance[N-1][N-1]))