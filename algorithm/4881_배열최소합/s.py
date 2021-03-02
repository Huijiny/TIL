import sys
sys.stdin = open("sample_input (1).txt")
def find(idx, sum_):
    global min_
    if idx == n:
        if min_ > sum_:
            min_ = sum_
            result
    if sum_ > min_:
        return
    else:
        for i in range(n):
            if visited[i] == False:
                visited[i] = True
                find(idx+1, sum_+matrix[idx][i])
                visited[i] = False
T = int(input())
for tc in range(1, T+1):
    result = 0
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [False for _ in range(n)]
    min_ = 99999999999
    find(0, 0)


    print("#{} {}".format(tc, min_))