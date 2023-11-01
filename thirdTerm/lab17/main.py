from parser import to_arr


def find(tree, elem, node=1):
    if tree[node] < elem:
        if tree[2 * node] == '-':
            return False
        else:
            return True
    if tree[node] == elem:
        return True
    if tree[node] > elem:
        if tree[2 * node + 1] == '-':
            return False
        else:
            return True


def insert(tree, elem, node=1):
    if node >= len(tree):
        for i in range(len(tree)):
            tree.append('-')
    if tree[node] == '-':
        tree[node] = elem
    elif elem < tree[node]:
        insert(tree, elem, 2 * node)
    elif elem > tree[node]:
        insert(tree, elem, 2 * node + 1)


def up(tree, node, depth=1, is_right=0):
    if (2 * node - node % depth + is_right * depth) < len(tree):
        tree[node] = tree[2 * node - node % depth + is_right * depth]
        up(tree, 2 * node, depth * 2, is_right)
        up(tree, 2 * node + 1, depth * 2, is_right)
    else:
        tree[node] = '-'


#12(7,15(,16(,19(17,20))))
def find_min(tree, node=1):
    if 2 * node < len(tree) and tree[2 * node] != '-':
        return find_min(tree, 2 * node)
    else:
        return node


def delete(tree, elem, node=1):
    if tree[node] != '-':
        if elem < tree[node] and 2 * node < len(tree):
            delete(tree, elem, 2 * node)
        if elem > tree[node] and 2 * node + 1 < len(tree):
            delete(tree, elem, 2 * node + 1)
        if elem == tree[node]:
            if 2 * node >= len(tree):
                tree[node] = '-'
            elif tree[2 * node] == '-' and tree[2 * node + 1] == '-':
                tree[node] = '-'
            elif tree[2 * node] != '-' and tree[2 * node + 1] == '-':
                up(tree, node, 1, 0)
            elif tree[2 * node] == '-' and tree[2 * node + 1] != '-':
                up(tree, node, 1, 1)
            else:
                node_next = find_min(tree, 2 * node + 1)
                tree[node] = tree[node_next]
                up(tree, node_next, 1, 1)

def show(tree, node=1, depth=0):
    if tree[node] != '-':
        print(tree[node], end='')
        if (2 * node < len(tree) and tree[2 * node] != '-') or (2 * node + 1 < len(tree) and tree[2 * node + 1] != '-'):
            print('(', end='')
        if 2 * node < len(tree) and tree[2 * node] != '-':
            show(tree, 2 * node, depth + 1)
        if (2 * node < len(tree) and tree[2 * node] != '-') or (2 * node + 1 < len(tree) and tree[2 * node + 1] != '-'):
            print(',', end='')
        if 2 * node + 1 < len(tree) and tree[2 * node + 1] != '-':
            show(tree, 2 * node + 1, depth + 1)
        if (2 * node < len(tree) and tree[2 * node] != '-') or (2 * node + 1 < len(tree) and tree[2 * node + 1] != '-'):
            print(')', end='')


print('Input tree:')
str_tree = input()
tree = to_arr(str_tree)
command = ''
while command != 'exit':
    print('Input command:')
    command = input()
    if command == 'insert':
        print('Input element:')
        elem = int(input())
        insert(tree, elem)
    elif command == 'delete':
        print('Input element:')
        elem = int(input())
        delete(tree, elem)
    elif command == 'show':
        show(tree)
        print()
    elif command != 'exit':
        print('Unknown command')

