def get(x, par):
    if par[x] != x:
        par[x] = get(par[x], par)
    return par[x]


def union(x, y, par, rang):
    x = get(x, par)
    y = get(y, par)
    if x == y:
        return
    if rang[x] == rang[y]:
        rang[x] += 1
    if rang[x] < rang[y]:
        par[x] = y
    else:
        par[y] = x


n = int(input())
E = []
for i in range(n):
    row = list(map(int, input().split(' ')))
    for j in range(n):
        if j >= i and row[j] > 0:
            E.append((row[j], (i, j)))
p = [i for i in range(n)]
r = [0] * n
E.sort(key=lambda x: x[0])
F = []
for i in range(len(E)):
    if get(E[i][1][0], p) != get(E[i][1][1], p):
        union(E[i][1][0], E[i][1][1], p, r)
        F.append((E[i][1][0], E[i][1][1]))
print(F)
