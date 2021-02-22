import sys
sys.stdin = open("input (3).txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N == 1:
        result = [[1]]
    else:
        result = [[1], [1, 1]]
        for col in range(2, N):
            tmp = [1]
            for row in range(1, col):
                tmp.append(result[col-1][row-1]+result[col-1][row])
            tmp.append(1)
            result.append(tmp)
    print("#{}".format(tc))
    for res in result:
        print(*res)