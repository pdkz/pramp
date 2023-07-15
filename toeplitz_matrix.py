from typing import List
from collections import defaultdict
def isToeplitz(arr: List[List]) -> bool:
    R, C = len(arr), len(arr[0])
    for j in range(C):
        v = arr[0][j]
        #for i in range(R-j):
        for i in range(min(R-j, C-j)):
            #print(arr[i][j+i], end=' ')
            if arr[i][j+i] != v:
                return False
        #print()

    for i in range(R):
        v = arr[i][0]
        #for j in range(R-i):
        print(i)
        for j in range(min(R-i, C-i)):
            print(f'{i+j},{j}')

            if arr[i+j][j] != v:
                return False
        #print()
    return True

def isToeplitz_diagonal_hash(arr: List[List]) -> bool:
    R, C = len(arr), len(arr[0])
    seen = defaultdict()
    for i in range(R):
        for j in range(C):
            if i-j not in seen:
                seen[i-j] = arr[i][j]
            else:
                if seen[i-j] != arr[i][j]:
                    return False
    return True

def main():
    matrix = [
        [1,2,3,4],
        [5,1,2,3],
        [6,5,1,2]]
    print(isToeplitz_diagonal_hash(matrix))

    matrix = [
        [1,2,3,4],
        [5,1,9,3],
        [6,5,1,2]]
    print(isToeplitz(matrix))

    # matrix = [
    #     [1,2],
    #     [3,1],
    #     [4,3]]
    # print(isToeplitz(matrix))

    # matrix = [[3],[5],[6]]
    # print(isToeplitz(matrix))

if __name__ == '__main__':
    main()