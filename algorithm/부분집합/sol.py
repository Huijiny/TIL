A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for i in range(1<<10):
    s = 0
    for j in range(10):
        if i & (1<<j):
            s += A[j]
            print(s)
    if s == 0:
        for j in range(10):
            if i & (1 << j):
                print(A[j], end='')
        print()