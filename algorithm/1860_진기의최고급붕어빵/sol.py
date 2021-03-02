import sys
sys.stdin = open("input (4).txt")

T = int(input())
for tc in range(1, T+1):
    result = "Possible"
    people, sec, bread = map(int, input().split())
    arrival_times = sorted(list(map(int, input().split())))
    i = 0
    p_count = 0
    for n in arrival_times:
        p_count += 1
        bread_count_at_moment = (n // sec) * bread
        if p_count > bread_count_at_moment:
            result = "Impossible"
            break
    print("#{} {}".format(tc, result))