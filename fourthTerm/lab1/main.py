def loc(a, b, c):
    return (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])


def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


# Jarvis march
def convex_hull(points):
    min_left = float('inf')
    for i in range(len(points)):
        if points[i][0] < min_left:
            min_left = points[i][0]
    min_low, start_pos = float('inf'), 0
    for i in range(len(points)):
        if (points[i][0] == min_left) and (points[i][1] < min_low):
            min_low = points[i][1]
            start_pos = i

    not_selected = [i for i in range(len(points))]
    selected = [start_pos]
    not_selected.remove(start_pos)
    not_selected.append(start_pos)
    while True:
        left = 0
        for i in range(1, len(not_selected)):
            if loc(points[selected[-1]], points[not_selected[left]], points[not_selected[i]]) > 0:
                left = i
        cur_pos = left
        max_dist = dist(points[selected[-1]], points[not_selected[cur_pos]])
        for i in range(len(not_selected)):
            if (selected[-1] != not_selected[left] and not_selected[left] != not_selected[i] and
                    selected[-1] != not_selected[i] and
                    (loc(points[selected[-1]], points[not_selected[left]], points[not_selected[i]]) == 0) and
                    dist(points[selected[-1]], points[not_selected[i]]) > max_dist):
                max_dist = dist(points[selected[-1]], points[not_selected[i]])
                cur_pos = i
       # print(cur_pos)
        if not_selected[cur_pos] == selected[0]:
            break
        else:
            selected.append(not_selected[cur_pos])
            del not_selected[cur_pos]
    return selected


n = int(input())
points = []
for i in range(n):
    points.append(tuple(map(int, input().split(' '))))
print(convex_hull(points))
