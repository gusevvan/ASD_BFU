def make_heap(arr):
    for i in range(len(arr) - 1, -1, -1):
        down(arr, start_index=i)

def down(arr, start_index=0):
    flag = True
    while start_index < len(arr) and flag:
        flag = False
        left, right = arr[start_index], arr[start_index]
        if 2 * start_index + 1 < len(arr):
            left = arr[2 * start_index + 1]
        if 2 * start_index + 2 < len(arr):
            right = arr[2 * start_index + 2]
        if left < arr[start_index] and left <= right:
            arr[start_index], arr[2 * start_index + 1] = arr[2 * start_index + 1], arr[start_index]
            start_index = 2 * start_index + 1
            flag = True
        elif right < arr[start_index] and right <= left:
            arr[start_index], arr[2 * start_index + 2] = arr[2 * start_index + 2], arr[start_index]
            start_index = 2 * start_index + 2
            flag = True


arr = [int(n) for n in input().split(' ')]
make_heap(arr)
sort_arr = []
for i in range(len(arr)):
    arr[0], arr[-1] = arr[-1], arr[0]
    sort_arr.append(arr[-1])
    arr.pop()
    down(arr)
print(sort_arr)
