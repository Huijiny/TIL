import sys
sys.stdin = open("input (4).txt")

T = int(input())
for tc in range(1, T+1):
    days = int(input())
    prices = list(map(int, input().split()))
    ans = 0
    max_ = prices[len(prices)-1]
    for i in range(len(prices)-2, -1, -1):
        if prices[i] > max_:
            max_ = prices[i]
        else:
            ans += max_ - prices[i]
    print("#{} {}".format(tc, ans))
