
N, M = map(int, input().split(" "))
area = [list(map(int,input().split(" "))) for i in range(N)]

#
direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
clouds = [[0 for _ in range(N)] for _ in range(N)]
clouds[N-1][0] = 1
clouds[N-1][1] = 1
clouds[N-2][0] = 1
clouds[N-2][1] = 1

new_clouds = []
for _ in range(M):
    dir, num = map(int, input().split(" "))
    dir -= 1
    # 모든 구름이 dir방향으로 nums칸 이동한다.
    for i in range(N):
        for j in range(N):
            # 이미 내린 애들이면 지나
            # if clouds[i][j] == 2:
            #     continue

            # 1이면 구름이 있는 애들이니깐
            if clouds[i][j] == 1:
                col = i
                row = j

                new_col = (N + col + direction[dir][0] * num) % N
                new_row = (N + row + direction[dir][1] * num) % N
                new_clouds.append((new_col, new_row))
                # 새로운 구름에 추가했으니까 0으로 바꿔
                clouds[i][j] = 0

    # 구름이 있는 칸에 비가 1씩 내리고 구름은 사라진다.
    for cloud in new_clouds:
        area[cloud[0]][cloud[1]] += 1
        clouds[cloud[0]][cloud[1]] = 2

    # 대각선 체크
    cdelcol = [-1, 1, -1, 1]
    cdelrow = [1, -1, -1, 1]
    for cloud in new_clouds:
        cnt = 0
        for i in range(4):
            new_col = cloud[0] + cdelcol[i]
            new_row = cloud[1] + cdelrow[i]

            if 0 <= new_col < N and 0 <= new_row < N: # 범위안에 있는 대각선이면,
                if area[new_col][new_row] > 0: # 물이 잇으면,
                    cnt += 1
        area[cloud[0]][cloud[1]] += cnt
    new_clouds = []
    # 구름이 있었던 칸을 제외한 나머지 칸 중 물의 양이 2 이상인 칸에 구름이 생김. 구름이 생기면 물의양이 2만큼 줄어든다.

    for i in range(N):
        for j in range(N):
            if clouds[i][j] != 0:
                clouds[i][j] = 0
                continue
            if area[i][j] >= 2:
                clouds[i][j] = 1
                area[i][j] -= 2

sum_ = 0
for i in range(N):
    for j in range(N):
       sum_ += area[i][j]
print(sum_)