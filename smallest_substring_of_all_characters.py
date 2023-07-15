from collections import Counter
def get_shortest_unique_substring(arr, str):
    size, N = float('inf'), len(str)
    window, ht = Counter(), Counter(arr)
    i, j, begin, end = 0, 0, 0, 0
    for i in range(0, N):
        window[str[i]] += 1
        print(window, all([window[k] >= v for k, v in ht.items()]))
        while all([window[k] >= v for k, v in ht.items()]):
            if i-j+1 < size:
                begin, end, size = j, i, i-j+1
            window[str[j]] -= 1
            j += 1
        i += 1
    print(j, i)
    while j < i:
        if all([window[k] >= v for k, v in ht.items()]):
            if i-j+1 < size:
                begin, end, size = j, i, i-j+1
        window[str[j]] -= 1
        j += 1
    print(begin, end, size, str[begin:end+1])
    return "" if size == float('inf') else str[j:i+1]

#get_shortest_unique_substring(["A"], "B")
get_shortest_unique_substring(["A"], "A")
#arr = ['x','y','z']
#s = "xyyzyzyx"
#get_shortest_unique_substring(arr, s)
