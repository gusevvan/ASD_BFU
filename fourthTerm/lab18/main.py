n = int(input())
a = list(map(int, input().split(' ')))
a.sort(key=lambda x: abs(x))
cur_sum = a[0]
min_sum = a[0]
a = a[1:]
for i in range(n - 1):
    diffs = []
    for j in range(len(a)):
        diffs.append((abs(cur_sum + a[j]), j))
    cur_sum = diffs[0][0]
    min_sum = min(min_sum, cur_sum)
    new_a = []
    for j in range(len(a)):
        if j != diffs[0][1]:
            new_a.append(a[j])
    a = new_a
print(min_sum)
