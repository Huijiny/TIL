import sys
sys.stdin = open("sample_input (3).txt")

def charging_bus(start, count):
    global min_count
    # 만약에 시작지점이 마지막 지점이면,
    if start >= last:
        # 카운트에서 마지막지점을 하나 빼 주면서 리턴한다.
        if min_count > count - 1:
            min_count = count - 1

    if min_count < count:
        return

    else:
        # 배터리가 갈 수 있는 1부터 최대용량까지의 거리를 다 가본다.
        battery_count = battery[start]
        for bat in range(1, battery_count+1):
            charging_bus(start + bat, count + 1)

T = int(input())
for tc in range(1, T+1):
    min_count = 99999
    values = list(map(int, input().split()))
    N = values[0]
    battery = values[1:] + [0]
    last = len(battery) - 1
    charging_bus(0, 0)
    print("#{} {}".format(tc, min_count))