import sys
sys.stdin = open("sample_input (3).txt")

T = int(input())
for tc in range(1, T+1):
    num = float(input())
    result = ''
    cnt = 0
    while cnt < 13:
        num *= 2
        result += str(int(num) % 2)
        cnt += 1
        if num % 1 == 0:
            break
    else:
        result = 'overflow'
    print("#{} {}".format(tc, result))