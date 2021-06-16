import sys
sys.stdin = open("sample.txt")

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

min_val = 9999999999
max_val = -9999999999
def backtrack(idx, value, operators):
    global min_val, max_val
    if idx == n:
        min_val = min(min_val, value)
        max_val = max(max_val, value)
        return
    else:
        if operators[0]:
            operators[0] -= 1
            backtrack(idx+1, value+numbers[idx], operators)
            operators[0] += 1
        if operators[1]:
            operators[1] -= 1
            backtrack(idx+1, value-numbers[idx], operators)
            operators[1] += 1
        if operators[2]:
            operators[2] -= 1
            backtrack(idx+1, value*numbers[idx], operators)
            operators[2] += 1
        if operators[3]:
            operators[3] -= 1
            backtrack(idx+1, int(value/numbers[idx]), operators)
            operators[3] += 1

backtrack(1, numbers[0], operators)

print(max_val)
print(min_val)
