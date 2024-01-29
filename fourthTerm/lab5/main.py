def dfs1(v, G, was, ord):
    was[v] = True
    for u in G[v]:
        if not was[u]:
            dfs1(u, G, was, ord)
    ord.append(v)


def dfs2(v, G, was, comp):
    comp.append(v)
    was[v] = True
    for u in G[v]:
        if not was[u]:
            dfs2(u, G, was, comp)


n = int(input())
G = [[] for i in range(n)]
H = [[] for i in range(n)]
for i in range(n):
    row = list(map(int, input().split(' ')))
    for j in range(n):
        if row[j] == 1:
            G[i].append(j)
for i in range(n):
    for j in G[i]:
        H[j].append(i)
was = [False] * n
ord = []
for i in range(n):
    if not was[i]:
        dfs1(i, H, was, ord)
num_copms = 0
was = [False] * n
comps = []
for i in ord[::-1]:
    if not was[i]:
        num_copms += 1
        comp = []
        dfs2(i, G, was, comp)
        comps.append(comp)
print(num_copms, comps)

