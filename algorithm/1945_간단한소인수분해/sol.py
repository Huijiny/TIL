import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    number = int(input())
    indices = [0, 0, 0, 0, 0]


    while number != 1:
        q = 0
        if not number % 2:
            indices[0] += 1
            q = 2
        elif not number % 3:
            indices[1] += 1
            q = 3
        elif not number % 5:
            indices[2] += 1
            q = 5
        elif not number % 7:
            indices[3] += 1
            q = 7
        elif not number % 11:
            indices[4] += 1
            q = 11

        number /= q

    print("#{} {} {} {} {} {}".format(tc,indices[0],indices[1],indices[2],indices[3],indices[4]))