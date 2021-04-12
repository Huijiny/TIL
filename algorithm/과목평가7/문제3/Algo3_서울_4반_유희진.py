dcol = [1, -1, 0, 0]
drow = [0, 0, 1, -1]

def bfs(robot):
    global result
    queue = [robot]
    distance = 0

    while queue:
        # 현재 로봇의 장소
        cur_col, cur_row = queue.pop(0)
        distance += 1
        # 현재 로봇 있는 장소가 3, 4, 5중에 하나라면,
        if ground[cur_col][cur_row] > 2:
            # zone이므로 이미 지나간 곳은 1로 벽 처리하기.
            ground[cur_col][cur_row] = 1
            zones[ground[cur_col][cur_row]][2] = True
            # 거리 추가하기
            result += distance

            # queue안에 있는거 비우고, 새롭게 그 자리부터 시작하기 위해서 현재 위치 넣고, 거리 초기화 시키기.
            queue.clear()
            queue.append((cur_col, cur_row))
            distance = 0
        # 새로운 인덱스 값 찾고,
        for i in range(4):
            new_col = cur_col + dcol[i]
            new_row = cur_row + drow[i]

            # 범위 내에 있고, 벽이 아니라면
            if 0 <= new_row < N and 0 <= new_row < N and ground[new_col][new_row] != 1:
                # 가야할 곳에 위치 추가
                queue.append((new_col, new_row))

T = int(input())

for tc in range(1, T+1):
    result = 0
    N = int(input())
    ground = [list(map(int, input().split())) for _ in range(N)]
    zones = []
    robot = 0
    for i in range(N):
        for j in range(N):
            if ground[i][j] == 2:
                robot = (i, j, False)
                ground[i][j] = 0
            elif ground[i][j] == 3:
                red_zone = (i, j, False)
            elif ground[i][j] == 4:
                green_zone = (i, j, False)
            elif ground[i][j] == 5:
                blue_zone = (i, j)
    zones.append(red_zone)
    zones.append(green_zone)
    zones.append(blue_zone)
    bfs(robot)
    print("#{} {}".format(tc, result))