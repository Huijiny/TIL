import sys

sys.stdin = open("sample_input.txt")

T = int(input())


def check(arr, N, K):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    if total == K and len(arr) == N:
        return True
    else:
        return False


for tc in range(1, T + 1):
    count = 0
    result = 0
    N, K = map(int, input().split())  # N개의 원소를 갖고 원소의 합이 K인 부분집합의 개수

    n = 12
    arr = list(range(1, n + 1))
    for i in range(1 << n):  # 원소의 개수 12개
        tmp_arr = []
        for j in range(n + 1):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
                count += 1
                tmp_arr.append(arr[j])
        if check(tmp_arr, N, K):
            result += 1

    print("#{} {}".format(tc, result))



