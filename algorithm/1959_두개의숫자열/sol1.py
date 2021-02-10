import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    values = []
    if N < M:
        counts = M-N+1
        for count in range(counts):
            value = 0
            for i in range(N):
                value += A[i] * B[i+count]
            values.append(value)
    elif M < N:
        counts = N-M+1
        for count in range(counts):
            value = 0
            for i in range(M):
                value += B[i] * A[i + count]
            values.append(value)
    elif M == N:
        value = 0
        for i in range(M):
            value += B[i] * A[i + count]
        values.append(value)

    maximum = values[0]
    for value in values:
        if maximum < value:
            maximum = value

    print('#{} {}'.format(tc, maximum))
