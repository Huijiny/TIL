import sys
sys.stdin = open("sample_input (1).txt")
T = int(input())


def dfs(idx, now_cal, now_grade):
    global max_grade
    if now_cal > limit:
        return
    if idx == n:
        if max_grade < now_grade:
            max_grade = now_grade
        return
    else:
        dfs(idx+1, now_cal+ingre[idx][1], now_grade+ingre[idx][0])
        dfs(idx+1, now_cal, now_grade)


for tc in range(1, 1+T):
    result = 0
    n, limit = map(int, input().split())
    ingre = []
    for i in range(n):
        ingre.append(list(map(int,input().split())))
    max_grade = 0
    dfs(0, 0, 0)

    print("#{} {}".format(tc, max_grade))
