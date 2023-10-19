from parser import to_arr

str_tree = input()
tree = to_arr(str_tree)
be_passed = [False] * len(tree)
cur_index = 1
while cur_index > 0:
    if not be_passed[cur_index]:
        print(tree[cur_index])
        be_passed[cur_index] = True
    if cur_index * 2 < len(tree):
        if not be_passed[cur_index * 2] and tree[cur_index * 2] != '-':
            cur_index *= 2
        elif not be_passed[cur_index * 2 + 1] and tree[cur_index * 2 + 1] != '-':
            cur_index = cur_index * 2 + 1
        else:
            cur_index //= 2
    else:
        cur_index //= 2
