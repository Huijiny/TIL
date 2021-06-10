def solution(n, arr):
    memo = [0] * 100

    def recursive(idx):
        if idx == 0:
            return 0
        if idx < 0:
            return -99999
        if memo[idx] != 0:
            return memo[idx]

        a = recursive(idx - 2)
        b = recursive(idx - 7)
        memo[idx] = max(a, b) + arr[idx]
        print(memo)
        return memo[idx]
    max_ = -999999999
    for i in range(1, 6):
        ret = recursive(n + i)
        if ret > max_:
            max_ = ret
    print(max_)

solution(14, [1, 50, 1, -1, 1, 3, -5, 1, -15, 0, 100, 1, 1, 2])