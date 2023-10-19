from sort import quicksort

N = 2
arrs = []
for i in range(N):
    f = open(f'text{i}.txt')
    arr = [int(n) for n in f.read().split(' ')]
    quicksort(arr, 0, len(arr) - 1)
    arrs.append(arr)
    f.close()
sorted_arr = []
pointers = [0] * N
min_arr = 0
while min_arr != -1:
    min_element = 1e20
    min_arr = -1
    for i in range(N):
        if pointers[i] < len(arrs[i]) and arrs[i][pointers[i]] < min_element:
            min_element = arrs[i][pointers[i]]
            min_arr = i
    if min_arr != -1:
        pointers[min_arr] += 1
        sorted_arr.append(min_element)
f = open('output.txt', 'w')
f.write(str(sorted_arr))
f.close()
