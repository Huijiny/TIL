import sys
sys.stdin = open("input (4).txt")


def is_safe(y, x):
    if 0 <= x < n and 0 <= y < n and matrix[y][x] != 0:
        return True
    return False
# def search_size(r, c):
#     r_cnt = 0
#     c_cnt = 0
#
#     #행의 크기를 찾는.
#     for i in range(r, N):
#         if arr[i][c] != 0:
#             r_cnt += 1
#         else:
#             break
#     # 열의 길이를 찾는
#     for i in range(c, N):
#         if arr[r][i] != 0:
#             c_cnt += 1
#         else:
#             break
#
#     ans.append([r_cnt, c_cnt, r_cnt*c_cnt])
#     init(r, c, r_cnt, c_cnt)

# 화학 물질들을 빈 용기로 변
# def init(r, c, r_cnt, c_cnt):
#     for i in range(r, r+r_cnt):
#         for j in range(c, c+c_cnt):
#             arr[i][j] = 0
#
#
# def counting_sort(idx):
#     cnt = [0] * 10001
#     sort_ans = [0] * len(ans)
#     for i in range(len(ans)):
#         cnt[ans[i][idx]] += 1
#
#     #2. 누적과정
#     for i in range(1, len(cnt)):
#         cnt[i] += cnt[i-1]
#
#     # 3. 실제로 정렬하여 넣는 과정
#     for i in range(len(ans)-1, -1, -1):
#         sort_ans[cnt[ans[i][idx]] -1] = ans[i]
#         cnt[ans[i][idx]] -= 1
#
#     return sort_ans
def bfs(col, row):
    queue = []
    queue.append((col, row))
    cur_c, cur_r = (0, 0)
    while queue:
        cur_c, cur_r = queue.pop(0)
        matrix[cur_c][cur_r] = 0
        dcol = [1, 0]
        drow = [0, 1]
        for i in range(2):
            new_col = dcol[i] + cur_c
            new_row = drow[i] + cur_r
            if is_safe(new_col, new_row):
                queue.append((new_col, new_row))
    return cur_c - col + 1, cur_r - row + 1


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    # visited = [[0] * n for _ in range(n)]
    sizes = []
    # 행 우선순회 방식으로 순회하면서 사각형의 시작 좌표를 구한다.
    for col in range(n):
        for row in range(n):
            if matrix[col][row] != 0:
                # search_size(row, col)
                last_c, last_r = bfs(col, row)
                sizes.append((last_c, last_r))

    # 정렬
    print("#{} {} {}".format(tc, len(sizes),' '.join(list(map(str, sizes)))))

    # ans = counting_sort(0) # 행을 기준으로 정렬
    # ans = counting_sort(2) # 행렬의 크기로 다시한 번 정렬
