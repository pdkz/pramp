arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
        'm', 'a', 'k', 'e', 's', '  ',
        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

# output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
#           'm', 'a', 'k', 'e', 's', '  ',
#           'p', 'e', 'r', 'f', 'e', 'c', 't' ]

N = len(arr)
i, j = 0, N-1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
print(arr)
begin = None
for i in range(0, N):
    if arr[i] == '  ' or i == N-1:
        end = i if i == N-1 else i-1
        print('ok', begin, end)

        while begin < end:
            arr[begin], arr[end] = arr[end], arr[begin]
            begin += 1
            end -= 1
        begin = None
        print(arr)
    else:
        print(i, begin)
        if begin == None:
            begin = i
print(arr)
