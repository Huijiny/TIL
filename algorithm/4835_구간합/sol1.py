import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    sum_prefix = [0] * (N+1)

    for i in range(1, N+1):
        sum_prefix[i] = sum_prefix[i-1] + numbers[i-1]

    minimum = maximum = sum_prefix[M]

    #
    for i in range(M, N+1):
        value = sum_prefix[i] - sum_prefix[i-M]
        if minimum > value:
            minimum = value
        if maximum < value:
            maximum = value
    print('#{} {}'.format(tc, maximum - minimum))