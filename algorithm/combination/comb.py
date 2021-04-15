def f(i, j, n, r): # i c[i], j 선택 구간의 시작
    if i==r:
        print(c)
    else:
        for k in range(j, n-r+i+1):
            c[i] = arr[k]
            f(i+1, k+1, n, r)
arr = [1, 2, 3, 4, 5]
c = [0]*3

# n개에서 r개를 고른다.
n = 5
r = 3
f(0, 0, n, r)


# def comb2(i, n, r):
#     if i==r:
#         print(c)
#     else:
#         for j in range(i, n-r+i+1):
#             c[i] = arr[i]
#             comb2(i+1, n, r)
#
#
# M = 5
# A = [1, 2, 3, 4, 5]
# for i in range(0, M-3+1):
#     for j in range(0, M-2+1):
#         for k in range(0, M-1+1):
#             print(A[i], A[j], A[k])