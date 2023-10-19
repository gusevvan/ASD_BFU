def quicksort(arr, left, right):
    if left < right:
        sep = partition(arr, left, right)
        quicksort(arr, left, sep)
        quicksort(arr, sep + 1, right)


def partition(arr, left, right):
    sep = arr[(left + right) // 2]
    i, j = left, right
    while i <= j:
        while arr[i] < sep:
            i += 1
        while arr[j] > sep:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return j


arr = [int(n) for n in input().split(' ')]
quicksort(arr, 0, len(arr) - 1)
print(arr)
