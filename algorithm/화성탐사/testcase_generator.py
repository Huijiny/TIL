import random

print(50)

# 2차원 배열의 가로 길이 N
N = 5

for i in range(16):
    if i != 15:
        for j in range(3):
            # 1부터 N 제곱까지
            numbers = list(range(1, N**2+1))
            random.shuffle(numbers)
            print(N)
            # 줄 바꿈을 위한 변수 k
            k = 0
            for i in numbers:

                if k == N:
                    print()
                    k = 0

                print(i, end=" ")
                k += 1

            # 0부터 N-1까지
            a = random.randrange(0, N)
            b = random.randrange(0, N)

            print()
            print(a, end=" ")
            print(b)

            # 0부터 N-1까지
            c = random.randrange(0, N)
            d = random.randrange(0, N)


            # 혹시라도 같으면
            if a == c and b == d:
                c = (a+3) % N
                d = (b+3) % N

            print(c, end=" ")
            print(d)

        N += 1
    else:
        for j in range(2):
            # 1부터 N 제곱까지
            numbers = list(range(1, N**2+1))
            random.shuffle(numbers)
            print(N)
            # 줄 바꿈을 위한 변수 k
            k = 0
            for i in numbers:

                if k == N:
                    print()
                    k = 0

                print(i, end=" ")
                k += 1

            # 0부터 N-1까지
            a = random.randrange(0, N)
            b = random.randrange(0, N)

            print()
            print(a, end=" ")
            print(b)

            # 0부터 N-1까지
            c = random.randrange(0, N)
            d = random.randrange(0, N)


            # 혹시라도 같으면
            if a == c and b == d:
                c = (a+3) % N
                d = (b+3) % N

            print(c, end=" ")
            print(d)