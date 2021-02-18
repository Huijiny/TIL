import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    result = 0
    idx = 0
    while idx != len(A):
        if A[idx:idx+len(B)] == B:
            result += 1
            idx += len(B)
        else:
            result += 1
            idx += 1

    print("#{} {}".format(tc, result))