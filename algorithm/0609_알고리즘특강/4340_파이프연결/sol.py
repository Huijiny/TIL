import sys
sys.stdin = open("sample_sample_input.txt")
from pprint import pprint
pipes = {
    1: ['l', 'r'],
    2: ['u', 'd'],
    3: ['d', 'r'],
    4: ['l', 'd'],
    5: ['l', 'u'],
    6: ['r', 'u'],
}

oppsite = {
    'l': 'r',
    'r': 'l',
    'u': 'd',
    'd': 'u',
}
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
T = int(input())

for tc in range(1, T + 1):
    result = 0

    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    tmp_area = []
    visited = []


    def bfs(x, y, length):
        q = [(x, y, length)]
        min_length = 99999999
        while q:
            cur_x, cur_y, length = q.pop()
            cur_pipe = area[cur_y][cur_x]
            visited.append((cur_y, cur_x))
            if cur_x == N - 1 and cur_y == N - 1:
                pprint(area)
                print(length)
                if min_length > length:
                    min_length = length
            # 현재 파이프
            can_go = pipes[cur_pipe]
            # 4방향 검사 및 범위내에있는지, 파이프가 존재하는지 체크
            for i in range(4):
                new_x, new_y = cur_x + dx[i], cur_y + dy[i]
                if 0 <= new_y < N and 0 <= new_x < N and area[new_y][new_x] != 0 and (new_y, new_x) not in visited:
                    next_pipe = area[new_y][new_x]
                    # 파이프가 있으면 현재파이프랑 연결될 수 있는지 체크
                    # go = 현재 연결될 수 있는 방향.
                    for go in can_go:
                        # 직선이면 현재 한번, 90으로 한 번 돌린다음 체크해봄
                        # 커브이면 현재랑, 90, -90 3방향 판단함.
                        # # 연결가능하면 다음에 추가
                        if go in pipes[next_pipe]:
                            q.append((new_x, new_y, length + 1))
                        # 연결될 수 없으면 회전 가능한지 보고 회전해
                        # else:
                        # 직선 파이프인경우
                        if 0 < cur_pipe < 3:
                            if cur_pipe == 1:
                                tmp_pipe = 2
                            else:
                                tmp_pipe = 1
                            if oppsite[go] in pipes[tmp_pipe]:
                                area[cur_y][cur_x] = tmp_pipe
                                q.append((new_x, new_y, length + 1))
                                area[cur_y][cur_x] = cur_pipe

                        # 커브 파이프인경우
                        elif cur_pipe >= 3:
                            for i in [-1, 1]:
                                tmp_pipe = cur_pipe + i
                                # 6이면 다음걸로 3이고.
                                if tmp_pipe == 7:
                                    tmp_pipe = 3
                                # 3이면 그 전걸로 6임.
                                elif tmp_pipe == 2:
                                    tmp_pipe = 6

                                if oppsite[go] in pipes[tmp_pipe]:
                                    area[cur_y][cur_x] = tmp_pipe
                                    q.append((new_x, new_y, length + 1))
                                    area[cur_y][cur_x] = cur_pipe

        return min_length


    result = bfs(0, 0, 0)
    print("#{} {}".format(tc, result))
