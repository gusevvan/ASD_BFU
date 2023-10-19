def to_arr(str_tree):
    max_depth = 1
    cur_depth = 1
    for char in str_tree:
        if char == '(':
            cur_depth += 1
            max_depth = max(max_depth, cur_depth)
        if char == ')':
            cur_depth -= 1
    tree = ['-'] * (2**max_depth)
    cur_index = 1
    cur_number = ''
    for char in str_tree:
        if char.isdigit():
            cur_number += char
        if char == '(':
            if len(cur_number) != 0:
                tree[cur_index] = int(cur_number)
                cur_number = ''
            cur_index *= 2
        if char == ',':
            if len(cur_number) != 0:
                tree[cur_index] = int(cur_number)
                cur_number = ''
            cur_index += 1
        if char == ')':
            if len(cur_number) != 0:
                tree[cur_index] = int(cur_number)
                cur_number = ''
            cur_index -= 1
            cur_index //= 2
        if char == ' ':
            pass
    return tree
