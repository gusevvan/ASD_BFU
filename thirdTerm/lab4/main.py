arr = []
arr = [int(n) for n in input().split(' ')]
step = len(arr) - 1
factor = 1.247
while step >= 1:
    for i in range(len(arr) - step):
        if arr[i] > arr[step + i]:
            arr[i], arr[step + i] = arr[step + i], arr[i]
    step = int(step / factor)
print(arr)