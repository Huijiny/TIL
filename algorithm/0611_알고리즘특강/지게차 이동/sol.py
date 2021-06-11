import sys
sys.stdin = open('sample')
# 답 18
# 답 6
# 다익스트라 활용해서 풀보기
H, W = map(int, input().split())

map_ = [list(map(int, input().split())) for _ in range(H)]

dx = [0, 1]
dy = [1, 0]

q = [(0, 0, 0)]

min_length = 99999999999
while q:
    print(q)
    cur_x, cur_y, length = q.pop()

    print(cur_x, cur_y, length)

    if cur_x == W-1 and cur_y == H-1:
        if min_length > length:
            min_length = length
    if min_length < length:
        continue

    new_x_d, new_y_d = cur_x+dx[0], cur_y+dy[0]
    new_x_r, new_y_r = cur_x+dx[1], cur_y+dy[1]

    if 0 <= new_x_d < W and 0 <= new_y_d < H and 0 <= new_x_r < W and 0 <= new_y_r < H:

        if map_[new_y_d][new_x_d] == map_[new_y_r][new_x_r]:
            new_x, new_y = new_x_d, new_y_d
            q.append((new_x, new_y, length+map_[new_y][new_x]))
        else:
            q.append((new_x_d, new_y_d, length+map_[new_x_d][new_y_d]))
            q.append((new_x_r, new_y_r, length+map_[new_x_r][new_y_r]))

print(min_length)



