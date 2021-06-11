import sys
sys.stdin = open('sample_input (5).txt')

T = int(input())

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
for tc in range(1, T+1):
    M, N, H = map(int, input().split())

    building = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    visited = []
    q = []
    humans = True
    cnt = 0

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if building[h][n][m] == 1:
                    q.append((h, n, m))

                if building[h][n][m] == -1:
                    humans = False
    if humans:
        q = []

    while q:
        for _ in range(len(q)):
            cur_h, cur_y, cur_x = q.pop()
            visited.append((cur_h, cur_y, cur_x))

            for i in range(6):
                new_h, new_y, new_x = cur_h + dz[i], cur_y + dy[i], cur_x + dx[i]
                if 0 <= new_h < H and 0 <= new_y < N and 0 <= new_x < M and building[new_h][new_y][new_x] == -1 and (new_h, new_y, new_x) not in visited:
                    building[new_h][new_y][new_x] = 1
                    q.append((new_h, new_y, new_x))
        cnt += 1

        human = True
        for h in range(H):
            for j in range(N):
                for i in range(M):
                    if building[h][j][i] == -1:
                        human = False
                        break
        if human == True:
            break
    result = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if building[h][n][m] == -1:
                    result = -1
                    break
    if result == -1:
     result = 'STILL ZOMBIES'
    elif humans:
        result = 'ALL HUMANS'
    else:
        result = cnt
    print("#{} {}".format(tc, result))