import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())
for tc in range(1, T+1):
    letters = input()
    stack = []
    for i in letters:
        if len(stack) == 0:
            stack.append(i)
        else:
            popped = stack.pop()
            if popped != i:
                stack.append(popped)
                stack.append(i)
    result = len(stack)
    print("#{} {}".format(tc, result))