import sys
sys.stdin = open("input (3).txt")
def solution(original):
    count = 0
    if original[0:1][0] == '1':
        count = 1
    for i in range(1, len(original)):
        if original[i-1] != original[i]:
            count += 1

    return count
T = int(input())
for tc in range(1, T+1):
    original = list(input())
    print("#{} {}".format(tc, solution(original)))