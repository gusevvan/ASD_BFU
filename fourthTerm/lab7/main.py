def down(q, k, ps, start_index=0):
    flag = True
    while start_index < len(q) and flag:
        flag = False
        left, right = k[start_index], k[start_index]
        if 2 * start_index + 1 < len(q):
            left = k[2 * start_index + 1]
        if 2 * start_index + 2 < len(q):
            right = k[2 * start_index + 2]
        if left < k[start_index] and left <= right:
            q[start_index], q[2 * start_index + 1] = q[2 * start_index + 1], q[start_index]
            k[start_index], k[2 * start_index + 1] = k[2 * start_index + 1], k[start_index]
            start_index = 2 * start_index + 1
            flag = True
        elif right < key[start_index] and right <= left:
            q[start_index], q[2 * start_index + 2] = q[2 * start_index + 2], q[start_index]
            key[start_index], key[2 * start_index + 2] = key[2 * start_index + 2], key[start_index]
            start_index = 2 * start_index + 2
            flag = True


n = int(input())
G = [[] for i in range(n)]
weights = []
for i in range(n):
    row = list(map(int, input().split(' ')))
    for j in range(n):
        if row[j] > 0:
            G[i].append(j)
    weights.append(row)
key = [float('inf')] * n
p = [0] * n
key[0] = 0
Q = [i for i in range(n)]
pos = [i for i in range(n)]
F = []
while len(Q) != 0:
    Q[0], Q[-1] = Q[-1], Q[0]
    v = Q[-1]
    pos[Q[-1]] = 0
    Q.pop()
    for u in G[v]:
        if u in Q and key[u] > weights[v][u]:
            p[u] = v
            key[u] = weights[v][u]
            down(Q, key, pos)
    F.append((v, p[v]))
print(F)

# 5
# 0 3 4 0 1
# 3 0 5 0 0
# 4 5 0 2 6
# 0 0 2 0 7
# 1 0 6 7 0
