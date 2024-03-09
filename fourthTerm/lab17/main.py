n, W = map(int, input().split(' '))
p = list(map(int, input().split(' ')))
cur_num = 1
while True:
    is_possible = False
    max_iter = cur_num ** n
    cur_iter = 0
    while cur_iter < max_iter:
        cur_pos = 1
        boxes = []
        for i in range(n):
            boxes.append((cur_iter // cur_pos) % cur_num)
            cur_pos *= cur_num
        cur_iter += 1
        is_correct = True
        s = [0] * cur_num
        for i in range(n):
            s[boxes[i]] += p[i]
            if s[boxes[i]] > W:
                is_correct = False
        is_possible = is_correct
        if is_possible:
            break
        cur_iter += 1
    if is_possible:
        print(cur_num)
        break
    cur_num += 1

