n = int(input())
G = []
for i in range(n):
    row = list(map(int, input().split()))
    G.append(row)
k = int(input())
max_iter = k**n
cur_iter = 0
is_colorable = False
while cur_iter < max_iter:
    cur_pos = 1
    coloring = []
    for i in range(n):
        coloring.append((cur_iter // cur_pos) % k)
        cur_pos *= k
    cur_iter += 1
    is_correct = True
    for u in range(n):
        for v in G[u]:
            if coloring[u] == coloring[v - 1]:
                is_correct = False
    is_colorable = is_correct
    if is_correct == True:
        break
print(is_colorable)
