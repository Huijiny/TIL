A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def bit():
    for i in range(1 << 10):
        for j in range(10):
            if i & (1 << j):
                print(A[j], end=' ')
        print()


def powerset(n, depth):
    global setA
    if depth == n:
        for i in range(n):
            if setA[i]:
                print(A[i], end=' ')
        print()
    else:
        setA[depth] = 0
        powerset(n, depth + 1)
        setA[depth] = 1
        powerset(n, depth + 1)

setA = [0] * len(A)
powerset(len(A), 0)

def bit1():
    for i in range(1 << len(A)):
        for j in range(len(A)):
            if i & (1 << j):
                print(A[j], end=' ')
        print()

bit1()


