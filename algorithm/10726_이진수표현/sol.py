import sys
sys.stdin = open("input (4).txt")

T = int(input())

for tc in range(1, T+1):
    N, num = map(int, input().split())
    bin = ''

    while num > 0:
        bin = str(num % 2) + bin
        num = num // 2
    result = 'ON'
    if len(bin) >= N:
        for i in range(len(bin)-N, len(bin)):
            if bin[i] == '0':
                result = 'OFF'
                break
    else:
        result='OFF'
    print("#{} {}".format(tc, result))