import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    while M > 0:
        queue.append(queue.pop(0))
        M -= 1
    print("#{} {}".format(tc,queue.pop(0) ))