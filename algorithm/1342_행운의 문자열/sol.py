import sys
sys.stdin = open("sample.txt")

s = input()
length = len(s)
cnt = 0
arr = [0] * 26
for i in s:
    arr[ord(i)-ord('a')] += 1


def backtrack(n, before):
    global cnt
    if n == length:
        cnt += 1

    for i in range(26):
        if i != before and arr[i] > 0:
            arr[i] -= 1
            backtrack(n+1, i)
            arr[i] += 1

backtrack(0, -1)
print(cnt)