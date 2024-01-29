from queue import Queue

n = int(input())
G = [[] for i in range(n)]
for i in range(n):
    row = list(map(int, input().split(' ')))
    for j in range(n):
        if row[j] == 1:
            G[i].append(j)
was = [False] * n
num_comps = 0
comps = []
for i in range(n):
    if not was[i]:
        comp = []
        q = Queue()
        q.put(i)
        was[i] = True
        comp.append(i)
        while not q.empty():
            i = q.get()
            for j in G[i]:
                if not was[j]:
                    was[j] = True
                    comp.append(j)
                    q.put(j)
        num_comps += 1
        comps.append(comp)
print(num_comps, comps)
