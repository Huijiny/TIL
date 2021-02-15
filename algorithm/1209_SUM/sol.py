import sys
sys.stdin = open('input (2).txt')

def check(results):
    max = results[0]
    for i in range(1, len(results)):
        if max < results[i]:
            max = results[i]
    return max



for tc in range(1, 11):
    num=int(input())
    result = 0
    N = 100
    matrix = []
    [matrix.append(list(map(int, input().split()))) for _ in range(N)]

    results = []
    for col in range(N):
        result = 0
        for row in range(N):
            result += matrix[col][row]
        results.append(result)

    for row in range(N):
        result = 0
        for col in range(N):
            result += matrix[col][row]
        results.append(result)

    right = 0
    left = 0
    for d in range(N):
        right += matrix[d][d]
        left += matrix[d][N-1-d]
    results.append(right)
    results.append(left)
    max = check(results)

    print("#{} {}".format(tc, max))