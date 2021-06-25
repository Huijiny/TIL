import sys
sys.stdin = open("sample.txt")

T = int(input())
for tc in range(1, T+1):
    strings = input()
    n = int(input())
    p = input()[1:-1].split(',')
    strings.replace("RR", "")

    F = 0
    B = 0
    R = 0
    for alpha in strings:
        if alpha == 'R':
            R += 1
        else:
            if R % 2 == 1:
                B += 1
            else:
                F += 1
    if F + B <= n:
        p = p[F:n - B]
        if R % 2 == 1:
            print('['+','.join(p[::-1])+']')
        else:
            print('['+','.join(p)+']')
    else:
        print("error")
