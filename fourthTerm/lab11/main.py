f = open('input.txt', 'r')
s = f.read()
t = input()
last = 0
links = [-1]
lens = [0]
edges = [{}]
firsts = [-1]
for c in s:
    cur = len(links)
    links.append(0)
    lens.append(lens[last] + 1)
    edges.append({})
    firsts.append(lens[cur] - 1)
    p = last
    while p >= 0 and c not in edges[p].keys():
        edges[p][c] = cur
        p = links[p]
    if p != -1:
        q = edges[p][c]
        if lens[p] + 1 == lens[q]:
            links[cur] = q
        else:
            new = len(links)
            links.append(links[q])
            lens.append(0)
            firsts.append(firsts[q])
            edges.append(edges[q])
            links[q] = new
            links[cur] = new
            lens[new] = lens[p] + 1
            while p >= 0 and edges[p][c] == q:
                edges[p][c] = new
                p = links[p]
    last = cur
cur = 0
is_substring = True
for c in t:
    if c in edges[cur]:
        cur = edges[cur][c]
    else:
        is_substring = False
if is_substring:
    print(firsts[cur] - len(t) + 1)
else:
    print(-1)
