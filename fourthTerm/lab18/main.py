n = int(input())
x = list(map(int, input().split(' ')))
s = [0]
for i in range(n):
    t = []
    for j in range(len(s)):
        t.append(s[j] + x[i])

