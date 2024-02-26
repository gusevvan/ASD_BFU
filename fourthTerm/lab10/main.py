def dfs(v, G, visited):
    visited[v] = True
    for u in G[v]:
        if not visited[u]:
            dfs(u, G, visited)


def is_eulerian(G):
    odd_degs = 0
    for i in range(len(G)):
        if len(G[i]) % 2 == 1:
            odd_degs += 1
    if odd_degs > 2:
        return False
    visited = [False] * len(G)
    for i in range(len(G)):
        if len(G[i]) > 0:
            dfs(i, G, visited)
            break
    for i in range(len(G)):
        if len(G[i]) > 0 and not visited[i]:
            return False
    return True


def find_euler_path(G):
    stack = []
    u = 0
    for i in range(len(G)):
        if len(G[i]) % 2 == 1:
            u = i
            break
    stack.append(u)
    while len(stack) != 0:
        w = stack[-1]
        found_edge = False
        for i in range(len(G)):
            if i in G[w]:
                stack.append(i)
                G[i].remove(w)
                G[w].remove(i)
                found_edge = True
                break
        if not found_edge:
            stack.pop()
            print(w)


def main():
    n = int(input())
    G = [[] for i in range(n)]
    for i in range(n):
        row = list(map(int, input().split(' ')))
        for j in range(n):
            if row[j] == 1:
                G[i].append(j)
    if is_eulerian(G):
        find_euler_path(G)
    else:
        print('Graph is not eulerian.')


main()


