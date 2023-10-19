from parser import to_arr

def NLR(tree, node=1):
    if node < len(tree) and tree[node] != '-':
        print(tree[node], end=' ')
        NLR(tree, 2 * node)
        NLR(tree, 2 * node + 1)

def LNR(tree, node=1):
    if node < len(tree) and tree[node] != '-':
        LNR(tree, 2 * node)
        print(tree[node], end=' ')
        LNR(tree, 2 * node + 1)

def LRN(tree, node=1):
    if node < len(tree) and tree[node] != '-':
        LRN(tree, 2 * node)
        LRN(tree, 2 * node + 1)
        print(tree[node], end=' ')

str_tree = input()
tree = to_arr(str_tree)
NLR(tree)
print()
LNR(tree)
print()
LRN(tree)
