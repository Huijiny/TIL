import sys
sys.stdin = open("sample.txt")

houses_cnt, wifis_cnt = map(int, input().split())
house_loc = []
for _ in range(houses_cnt):
    house_loc.append(int(input()))

house_loc.sort()
start = 1
end = house_loc[-1]-house_loc[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    start_house = house_loc[0]
    cnt = 1

    for i in range(1, len(house_loc)):
        if house_loc[i] >= start_house + mid:
            cnt += 1
            start_house = house_loc[i]

    # 카운트 했는데 설치해야하는 곳 보다 적으면 설치를 더 많이 해야하니까 간격을 좁혀
    if cnt < wifis_cnt:
        end = mid - 1
    # 설치해야하는 개수보다 이번에 센개 더 크면 너무 많이 설치한거라 좀 줄여야해서 간격을 넓혀
    # result를 저장하는 이유는 다음번에 개수를 만족시키지 못해서 while문이 종료될수 있기 때문
    else:
        start = mid + 1
        result = mid
print(result)