import sys
sys.stdin = open("sample_input.txt")
T = int(input())
for tc in range(1, T+1):
    steals = input()
    steals = steals.replace('()', 'B')
    sticks = []
    stick = sliced = 0

    for bracket in steals:
        if bracket == '(':
            sticks.append(bracket)
            sliced += 1
        elif bracket == ')':
            sticks.pop()
        else:
            sliced += len(sticks)

    print("#{} {}".format(tc, sliced))
