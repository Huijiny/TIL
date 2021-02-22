import sys
sys.stdin = open("sample_input.txt")



T = int(input())
for tc in range(1, T+1):
    arr = list(range(1, 13))
    N, K = map(int, input().split())
    length = len(arr)
    count = 0
    for i in range(1 << length):
        sub = []
        for j in range(length + 1):
            if i & (1 << j):
                sub.append(arr[j])
        if N == len(sub) and K == sum(sub):
            count += 1

    print("#{} {}".format(tc, count))