import sys
sys.stdin = open("input (4).txt")

# def counting_sort(idx):
#     cnt = [0] * 10001
#     sort_ans = [0] * len(sizes)
#     for i in range(len(sizes)):
#         cnt[sizes[i][idx]] += 1
#
#     #2. 누적과정
#     for i in range(1, len(cnt)):
#         cnt[i] += cnt[i-1]
#
#     # 3. 실제로 정렬하여 넣는 과정
#     for i in range(len(sizes)-1, -1, -1):
#         sort_ans[cnt[sizes[i][idx]] -1] = sizes[i]
#         cnt[sizes[i][idx]] -= 1
#
#     return sort_ans

def search_size(col, row):
    cnt_r = cnt_c = 0
    for i in range(col, n):
        if matrix[i][row] != 0:
            cnt_c += 1
        else:
            break
    for i in range(row, n):
        if matrix[col][i] != 0:
            cnt_r += 1
        else:
            break

    for i in range(col, col+cnt_c):
        for j in range(row, row+cnt_r):
            matrix[i][j] = 0

    sizes.append([cnt_c, cnt_r])


T = int(input())

for tc in range(1, 1+T):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    sizes = []
    # 행 우선순회 방식으로 순회하면서 사각형의 시작 좌표를 구한다.
    for col in range(n):
        for row in range(n):
            if matrix[col][row] != 0:
                search_size(col, row)

    sizes.sort(key=lambda x : (x[0] * x[1], x[0]))

    print("#{} {}".format(tc, len(sizes)), end=" ")
    for i in sizes:
        print("{} {}".format(i[0], i[1]), end=" ")
    print()