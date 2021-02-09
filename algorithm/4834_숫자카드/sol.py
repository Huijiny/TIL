import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    length = int(input())
    cards = list(map(int, list(input())))
    counts = [0] * 10

    for card in cards:
        counts[card] += 1

    max_count = counts[0]
    max_value = 0
    for idx, count in enumerate(counts):
        if max_count <= count:
            max_value = idx
            max_count = count

    print("#{} {} {}".format(tc, max_value, max_count))




