import sys
sys.stdin = open("sample_input.txt")


T = int(input())
for tc in range(1, T + 1):
    opt = list(input())
    letters = list(input())
    dit = {}
    max = 0
    for i in range(len(opt)):
        dit[opt[i]] = dit.get(opt[i], 0)
    for letter in letters:
        if dit.get(letter) != None:
            dit[letter] += 1
            if max < dit[letter]:
                max = dit[letter]
    print("#{} {}".format(tc, max))
