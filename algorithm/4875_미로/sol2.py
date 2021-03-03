import sys
sys.stdin = open("sample_input (1).txt")
########## 정석코드!!!! 그리고 visited가 사실 없어도 된다!!!!!***
def dfs(x, y):
    global found
    visited[y][x] = True

    if matrix[y][x] == 3:
        found = 1
        print('Find!')
    else:
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        for idx in range(4):
            dyn, dxn = dy[idx], dx[idx]
            # 1. 이동하려는 좌표값이 0 <= x, y < N을 만족하는지
            if 0 <= x + dxn < N and 0 <= y + dyn < N:
                # 2. 벽이 아닌가(길, 목적지, 출발지)
                if matrix[y+dyn][x+dxn] != 1:
                    # 3. 방문 했는지..?
                    if not visited[y + dyn][x + dxn]:
                        dfs(x + dxn, y + dyn)
            dfs(x+dxn, y+dyn)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 2:
                start = (x, y)
            elif matrix[y][x] == 3:
                goal = (x, y)
    visited = [[False for _ in range(N)] for _ in range(N)]
    found = 0
    dfs(*start)

    print("#{} {}".format(tc, found))