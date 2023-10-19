f = open('input.txt')
input = f.read()
f.close()
hash_table = []
for i in range(1000):
    hash_table.append([])
for line in input.split('\n'):
    for word in line.split(' '):
        hash_table[len(word)].append(word)
f = open('output.txt', 'w')
for i in range(1000):
    if len(hash_table[i]) != 0:
        f.write(str(i) + ': ')
        for word in hash_table[i]:
            f.write(word + ' ')
        f.write('\n')
f.close()
