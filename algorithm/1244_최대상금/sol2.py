from collections import deque
import sys
sys.stdin = open('input (4).txt')


w = [1, 10, 100, 1000, 10000, 100000]


def swap(n, i, j):
    a = (n // w[i]) % 10
    b = (n // w[j]) % 10
    return n - a * w[i] + (a * w[j]) - (b * w[j]) + (b * w[i])

print(swap(1234, 1, 3))
T = int(input())
for tc in range(1, T+1):
    num, cnt = input().split()
    N = len(num)
    num, cnt = int(num), int(cnt)

    visited = [[] for _ in range(12)]
    ans = 0
    dq = deque()
    dq.append((num, 0))

    while dq:
        n, k = dq.popleft()
        if k == cnt:
            ans = max(ans, n)
        else:
            for i in range(N-1):
                for j in range(i + 1, N):
                    val = swap(n, i, j)
                    if val in visited[k + 1]:
                        continue
                    visited[k + 1].append(val)
                    dq.append((val, k+1))
    print("#{} {}".format(tc, ans))