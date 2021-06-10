memo = [[-1, -1, -1, -1, -1] for _ in range(4)]
# dp..는 무리
# bfs 두 개 다 풀어보기
# 답은 6회

def solution(cave):
    global memo
    start = 0
    end = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        for j in range(5):
            if cave[i][j] == 'A':
                start = (i, j)
            if cave[i][j] == 'B':
                end = (i, j)
    memo[start[0]][start[1]] = 0
    current = 'A'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(cave):
    for i in range(4):
        for j in range(5):
            if cave[i][j] == 'A':
                starty = i
                startx = j
            if cave[i][j] == 'B':
                endy = i
                endx = j
    q = [(starty, startx, 0)]
    visited = []
    min_ = 999999999
    while q:

        cur_y, cur_x, length = q.pop()
        if cur_y == endy and cur_x == endx:
            if min_ > length:
                min_ = length
        visited.append((cur_y, cur_x))
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= new_y < 4 and 0 <= new_x < 5 and cave[new_y][new_x] != '#' and (new_y, new_x) not in visited:
                q.append((new_y, new_x, length + 1))
    print(min_)


bfs([['_', '#', '#', '#', '_'], ['_','_','_','_','_'], ['_', '#', '_', '#', '_'],['#', '#', 'A', '#', 'B'],])