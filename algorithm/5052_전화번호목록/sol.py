import sys
sys.stdin = open("sample.txt")

T = int(input())

for _ in range(T):
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(input())

    numbers.sort()
    flag = True
    for i in range(len(numbers) - 1):
        if numbers[i] in numbers[i + 1][:len(numbers[i])]:
            flag = False
            break

    if flag:
        print("YES")

    else:
        print("NO")