from functools import cmp_to_key

def cmp(a, b):
    if abs(a) == abs(b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    elif abs(a) < abs(b):
        return -1
    else:
        return 1

def absSort(arr):
    def smaller(a, b):
        if abs(a) < abs(b): return True  # 絶対値が小さい場合は真 -2, -7なら普通は -7,-2になるがこの場合は逆
        if abs(a) > abs(b): return False
        return a < b
    for i in range(len(arr)):
        best = i
        for j in range(i+1, len(arr)):
            if smaller(arr[j], arr[best]):
                best = j
        arr[best], arr[i] = arr[i], arr[best]
    return arr

if __name__ == '__main__':
    arr = [2, -7, -2, -2, 0]
    print(sorted(arr, key=cmp_to_key(cmp)))
    print(absSort(arr))