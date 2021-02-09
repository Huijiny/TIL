import sys
sys.stdin = open('input.txt')

T = int(input())
# [1,1,1,1,1,1]
# [1,2,3,1,2,3]
for tc in range(1, T+1):
    cards = list(map(int, list(input())))

    counter = [0] * 10
    is_babygin = 0

    for card in cards:
        counter[card] += 1

    i = 0
    while i < len(counter):
        if counter[i] >= 3:
            is_babygin += 1
            counter[i] -= 3
            continue

        if i < len(counter)-2:
            if counter[i] and counter[i+1] and counter[i+2]:
                is_babygin += 1
                counter[i] -= 1
                counter[i+1] -= 1
                counter[i+2] -= 1
                continue
        i += 1

    if is_babygin == 2:
        result = 1
    else:
        result = 0

    print('{} {}'.format(tc, result))