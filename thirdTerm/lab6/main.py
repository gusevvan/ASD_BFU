arr = [int(n) for n in input().split(' ')]
for i in range(len(arr)):
    min_elem = arr[i]
    min_index = i
    for j in range(i, len(arr)):
        if arr[j] < min_elem:
            min_elem = arr[j]
            min_index = j
    arr[min_index], arr[i] = arr[i], arr[min_index]

print(arr)