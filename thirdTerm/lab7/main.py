arr = [int(n) for n in input().split(' ')]
step = len(arr) // 2
while step > 0:
    for i in range(step, len(arr)):
        j = i
        while j >= step and arr[j - step] > arr[j]:
            arr[j - step], arr[j] = arr[j], arr[j - step]
            j -= step
    step //= 2
print(arr)
