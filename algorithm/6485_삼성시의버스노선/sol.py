import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus_lines = [0]*N
    for n in range(N):
        bus_lines[n] = tuple(map(int, input().split()))

    bus_stops = {}
    for i in range(1, 5001):
        bus_stops[i] = 0

    P = int(input()) # 버정갯수
    stop_names = []
    for _ in range(P):
        stop_names.append(int(input()))

    for bus_line in bus_lines:
        for i in range(bus_line[0], bus_line[1]+1):
            bus_stops[i] += 1

    output = []
    for stop_name in stop_names:
        output.append(str(bus_stops.get(stop_name)))

    print("#{} {}".format(tc, ' '.join(output)))