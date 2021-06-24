import sys
sys.stdin = open("sample.txt")

n, k = map(int, input().split())

def backtrack(num, numbers):
    global cnt
    if num == n:
        cnt += 1
        if cnt == k:
            print(''.join(numbers)[:-1])
            exit(1)
        return
    elif num > n:
        return
    else:
        for i in [1, 2, 3]:
            backtrack(num + i, numbers+[str(i)+'+'])

cnt = 0
backtrack(0, [])
print(-1)

