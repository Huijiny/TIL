import sys
sys.stdin = open("sample_input (3).txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    time = []
    for i in range(N):
        s, e = map(int, input().split())
        time.append([s, e])
    time.sort(key=lambda x:(x[1]))
    result = [time[0]]
    print(time)
    for i in range(1, N):
        # 이전 타임 종료 시간이 이후 타임 시작 타임보다 작다면,
        if result[len(result)-1][1] <= time[i][0]:
            result.append(time[i])
        else:
            continue
    print("#{} {}".format(tc, len(result)))