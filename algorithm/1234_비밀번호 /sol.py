import sys
sys.stdin = open("input (3).txt")
T = 10

for tc in range(1, T+1):
    numbers = list(input().split()[1])
    stack = []
    for num in numbers:
        if len(stack) == 0:
            stack.append(num)
        else:
            tmp = stack.pop()
            if tmp != num:
                stack.append(tmp)
                stack.append(num)
    print("#{} {}".format(tc, ''.join(stack)))