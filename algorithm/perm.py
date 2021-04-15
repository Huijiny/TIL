arr = [1, 2, 3]
is_babygin = False
def perm(idx, length):
    global is_babygin
    if not is_babygin:
        if idx == length:
            p = 0
            if arr[0] == arr[1] == arr[2]:
                p += 1
            if arr[3] == arr[4] == arr[5]:
                p += 1
            if arr[0] + 1 == arr[1] + 1 == arr[2]:
                p += 1
            if arr[3] + 1 == arr[4] + 1 == arr[5]:
                p += 1

            if p == 2:
                is_babygin = True
                print("BABYGIN", arr)
        else:
            for changer in range(idx, length):
                arr[idx], arr[changer] = arr[changer], arr[idx]
                perm(idx + 1, length)
                arr[idx], arr[changer] = arr[changer], arr[idx]