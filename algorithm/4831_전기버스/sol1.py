import sys
sys.stdin = open('sample_input.txt')

T = int(input())
# K = 한 번의 충전으로 최대한 이동할 수 있는 정류장 수
# end = 종점 N번 정류장 버스는 0~N까
# M = 충전기가 설치된 정류장 번호의 총 갯수


for tc in range(1, T+1):
    K, end, M = list(map(int, input().split()))
    charge_place = list(map(int, input().split()))
    charge_count = 0
    current = 0

    # 0부터 종점까지 돌면서

    result = 0
    while current <= end:
        if current+K >= end: #종점
            break
        else: # 종점아니면
            charged_idx = [] # 충전할 인덱스 저장할 공간
            for next in range(current+1, current+K+1):
                if next in charge_place:
                    charged_idx.append(next)
                if len(charged_idx) > 1:
                    charged_idx.pop(0)
            if len(charged_idx) == 0:
                charge_count = 0
                break
            else:
                current = charged_idx[0]
                charge_count += 1

    print("#{} {}".format(tc, charge_count))



