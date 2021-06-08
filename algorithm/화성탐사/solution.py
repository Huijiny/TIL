import sys
from pprint import pprint
sys.stdin = open('sample2')
T = int(input())
for tc in range(1, T+1):
    m = int(input())
    area = [list(map(int,input().split())) for _ in range(m)]
    starty, startx = map(int, input().split())
    endy, endx = map(int, input().split())

    q = [(starty, startx)]
    angle_count = 0
    dx = [0, 0, -1, 1, 1, -1, 1, -1]
    dy = [-1, 1, 0, 0, -1, 1, 1, -1]
    prev_dx = 0
    prev_dy = 0
    while q:
        cury, curx = q.pop()
        area[cury][curx] = -1
        # 만약에 현재 점이 도착지라면 그만한다.
        if cury == endy and curx == endx:
            break
        # 현재점이 도착지가 아니라면,
        else:
            minimum = m*m
            cur_dx, cur_dy = 0, 0
            minx, miny = -1, -1
            for i in range(8):
                newy, newx = cury+dy[i], curx+dx[i]
                # 만약에 델타가 포함된 새로운 좌표들이 -1값이 아니고 범위 내에 존재한다면
                if 0 <= newy < m and 0 <= newx < m and area[newy][newx] != -1:
                    # minimum 값과 그 좌표를 찾는다.
                    if minimum >= area[newy][newx]:
                        minimum = area[newy][newx]
                        minx, miny = newx, newy
                        cur_dx, cur_dy = dx[i], dy[i]
            # 만약 8방향 탐색 후에도 minx, miny 가 초기값과 같다면 더이상 움직일 수 있는 칸이 없는 것이므로, 0으로 초기화 후 while문 탈출
            if minx == -1 and miny == -1:
                angle_count = 0
                break
            # 만약 이전 방향과 현재 방향이 다르다면 angle_count를 올려준다.
            if cur_dx != prev_dx or cur_dy != prev_dy:
                prev_dx, prev_dy = cur_dx, cur_dy
                angle_count += 1
            # queue에 탐색할 다음 좌표로 추가한다.
            q.append((miny, minx))

    print("#{} {}".format(tc, angle_count-1))








