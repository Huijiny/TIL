import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    lenth = int(input())
    apts = list(map(int, input().split()))
    total_houses = 0

    for i in range(2, lenth-2):
        # 바로 옆에 있는 인덱스가 나보다 큰게 하나라도 있으면 continue
        if apts[i] <= apts[i+1] or apts[i] <= apts[i-1] or apts[i] <= apts[i+2] or apts[i] <= apts[i-2]:
            continue
        else:
            gaps = []
            for j in range(1, 3):
                gaps.append(apts[i] - apts[i-j])
                gaps.append(apts[i] - apts[i+j])

            min = 255
            for j in range(len(gaps)):
                if gaps[j] > 0 and gaps[j] < min:
                    min = gaps[j]

            total_houses += min

    print("#{} {}".format(tc, total_houses))