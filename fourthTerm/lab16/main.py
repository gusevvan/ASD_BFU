def find_ans(k, s):
    if a[k][s] == 0:
        return
    if a[k - 1][s] == a[k][s]:
        find_ans(k - 1, s)
    else:
        find_ans(k - 1, s - w[k])
        ans.append(k + 1)


W, n = map(int, input().split(' '))
w = list(map(int, input().split(' ')))
p = list(map(int, input().split(' ')))
a = [[0] * W for _ in range(n)]
for k in range(1, n):
    for s in range(1, W):
        if s >= w[k]:
            a[k][s] = max(a[k - 1][s], a[k - 1][s - w[k]] + p[k])
        else:
            a[k][s] = a[k - 1][s]

ans = []
find_ans(n - 1, W - 1)
print(ans)
