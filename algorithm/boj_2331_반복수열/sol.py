import sys
sys.stdin = open("input.txt")


def dfs(number):
    visited[number] += 1
    if visited[number] == 3:
        count = 0
        for i in range(len(visited)):
            if visited[i] == 1:
                count += 1
        print(count)
        return
    else:
        tot = 0
        for i in str(number):
            q, r = divmod(int(i), 10)
            tot += pow(r, P)
        dfs(tot)


A, P = map(int, input().split())
visited = [0] * 1000000

visited[A] += 1
q, r = divmod(A, 10)
total = 0
for i in str(A):
    q, r = divmod(int(i), 10)
    total += pow(r, P)

dfs(total)
