n = int(input())
G = [[] for i in range(n)]
weights = []
for i in range(n):
    row = list(map(int, input().split(' ')))
    for j in range(n):
        if row[j] > 0:
            G[i].append(j)
    weights.append(row)
F = [0]
is_in_F = [False] * n
is_in_F[0] = True
Q = []
min_weight, min_path = float('inf'), 0
for u in G[0]:
    if weights[0][u] < min_weight:
        min_weight = weights[0][u]
        min_path = u
Q.append((0, min_path, min_weight))
res = []
while len(Q) > 0:
    min_weight, min_start, min_path = float('inf'), 0, 0
    for u, v, weight in Q:
        if weight < min_weight:
            min_weight = weight
            min_start = u
            min_path = v
    F.append(min_path)
    res.append((min_start, min_path))
    is_in_F[min_path] = True
    Q = []
    for i in range(n):
        if is_in_F[i]:
            min_weight, min_path = float('inf'), -1
            for j in G[i]:
                if not is_in_F[j] and weights[i][j] < min_weight:
                    min_weight = weights[i][j]
                    min_path = j
            if min_path != -1:
                Q.append((i, min_path, weight))
print(res)

