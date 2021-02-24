N = 10
arr = [0] * N

data = list(range(1, 11))
is_selected = [None] * len(data)
results = []

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

def power_set(idx):
    if idx < len(data):
        is_selected[idx] = True
        power_set(idx+1)
        is_selected[idx] = False
        power_set(idx+1)
    else:
        total = 0
        for i in range(len(data)):
            if is_selected[i]:
                total += data[i]
        if total == 10:
            results.append(is_selected[:])
        return None


powerset(0)

arr1 = [1, 2, 3]
N = 3

sel = [0] * N # 결과들ㅇ이 저장될 리스트
check = [0] * N # 해당 원소를 사용했는지 안했는지에 관한 체크

def perm(idx):
    # 다 뽑아서 정리했다면.
    if idx == len(N):
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0: # 아직 이 값을 안썼다면?
                sel[idx] = arr1[i] # 값을 써라.
                check[i] = 1 # 사용했다는 표시
                perm(idx+1) # 한단계 더 내려가,
                check[i] = 0# 다음을 위해서 사용 안한 것 처럼 원상복구


def perm2(idx, check):
    if idx == N:
        print(sel)
        return

    for j in range(N):
        if check & (1<<j): continue

        sel[idx] = arr[j]
        perm(idx+1, check | (1<<j))

def perm_swap(idx):
    if idx == N:
        print(arr)
    else:
        for i in range(idx, N):
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx + 1)
            arr[idx], arr[i] = arr[i], arr[idx]