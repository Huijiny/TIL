N = 10
arr = [0] * N
def powerset(idx):
    if idx == N-1:
        count = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count += i+1
        if count == 10:
            print(*arr)

    else:
        idx += 1
        arr[idx] = 0
        powerset(idx)
        arr[idx] = 1
        powerset(idx)


powerset(0)