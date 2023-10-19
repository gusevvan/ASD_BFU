def sort(arr, pos=0):
    if pos == 0:
        for i in range(len(arr)):
            arr[i] = str(arr[i]).zfill(20)
    if pos == 20:
        for i in range(len(arr)):
            j = 0
            while j < 19 and arr[i][j] == '0':
                j += 1
            arr[i] = int(arr[i][j:])
        return arr
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    chars_cnt = dict(zip(chars, [0] * 10))
    for element in arr:
        chars_cnt[element[pos]] += 1
    count = 0
    for j in chars_cnt.keys():
        tmp = chars_cnt[j]
        chars_cnt[j] = count
        count += tmp
    seps = chars_cnt.copy()
    sorted_arr = arr.copy()
    for j in range(len(arr)):
        sorted_arr[chars_cnt[arr[j][pos]]] = arr[j]
        chars_cnt[arr[j][pos]] += 1
    result = []
    keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for j in range(9):
        if seps[keys[j + 1]] - seps[keys[j]] != 0:
            result.extend(sort(sorted_arr[seps[keys[j]]: seps[keys[j + 1]]], pos + 1))
    return result

arr = [int(n) for n in input().split(' ')]

print(sort(arr))
