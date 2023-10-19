arr = []
arr = [int(n) for n in input().split(' ')]

for i in range(len(arr)):
    j = i - 1
    while j >= 0 and arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        j -= 1

print(arr)
