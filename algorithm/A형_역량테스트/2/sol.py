import sys
sys.stdin = open("sample_input (5).txt")

def zeroSum():
    times = []
    for task in tasks:
        time, linked = task
        times.append(time)
    max_time = max(times)
    times.remove(max_time)
    times.append(int(max_time / 2))
    return max(times)

def checkCirculate(linked):
    start = []
    start_cnt = 0
    for i in range(len(linked)):
        if len(linked[i]) == 1 and linked[i][0] == 0:
            start.append(i)
            start_cnt += 1

    return False

def simulate(linked, tasks):
    # 만약에 연결되어있는게 아무것도 없다면?
    linkedsum = 0
    for link in linked:
        linkedsum += sum(link)

    if linkedsum == 0:
        return zeroSum()

    # 만약 하나라도 연결되어있다면?
    if checkCirculate(linked):
        return -1

    return 0

T = int(input())
for tc in range(1, T+1):
    result = 0
    n = int(input())
    tasks = []
    linked = []
    for i in range(n):
        arr = list((map(int, input().split(" "))))
        linked.append(arr[1:])
        tasks.append(arr)
    result = simulate(linked, tasks)

    print("#{} {}".format(tc, result))