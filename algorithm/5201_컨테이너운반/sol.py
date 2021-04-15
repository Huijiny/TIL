import sys
sys.stdin = open("sample_input (3).txt")

T = int(input())
for tc in range(1, T+1):
    result = 0
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    weights = sorted(weights, reverse=True)
    trucks = sorted(trucks, reverse=True)

    i, j = 0, 0
    while i < M and j < N:
        if trucks[i] >= weights[j]:
            result += weights[j]
            i += 1
            j += 1
        else:
            j += 1
    print("#{} {}".format(tc, result))