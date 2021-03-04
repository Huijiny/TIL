import sys
sys.stdin = open("input")
def dfs(i):
    visited[i] = True
    if not visited[numbers[i-1]]:
        dfs(numbers[i-1])

T = int(input())
for _ in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    visited = [0] * (N+1)
    count = 0
    for i in range(1, len(numbers)+1):
        if not visited[i]:
            dfs(i)
            count += 1
    print(count)