def sort(arr):
    if len(arr) == 1:
        return arr
    left, right = arr[:len(arr) // 2], arr[len(arr) // 2:]
    sorted_left, sorted_right = sort(left), sort(right)
    result = []
    left_index, right_index = 0, 0
    while left_index < len(sorted_left) or right_index < len(sorted_right):
        if left_index < len(sorted_left):
            if right_index < len(sorted_right):
                if sorted_left[left_index] < sorted_right[right_index]:
                    result.append(sorted_left[left_index])
                    left_index += 1
                else:
                    result.append(sorted_right[right_index])
                    right_index += 1
            else:
                result.append(sorted_left[left_index])
                left_index += 1
        else:
            result.append(sorted_right[right_index])
            right_index += 1
    return result

arr = [int(n) for n in input().split(' ')]
print(sort(arr))
