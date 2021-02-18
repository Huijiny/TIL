import sys
sys.stdin = open("sample_input.txt")

def solution(s, l):
    for i in range(len(l)):
        if l[i:i+len(s)] == s:
            return 1
    return 0
# def solution(s, l):
#     if s in l:
#         return 1
#     else:
#         return 0
T = int(input())
for tc in range(1, T + 1):
    short = input()
    long = input()

    print("#{} {}".format(tc, solution(short, long)))