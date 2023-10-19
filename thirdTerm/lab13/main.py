f = open('input.txt')
input = f.read()
f.close()
hash_table = [''] * 100000
for line in input.split('\n'):
    for word in line.split(' '):
        i = len(word)
        while hash_table[i] != '':
            i += 1
        hash_table[i] = word
f = open('output.txt', 'w')
for i in range(100000):
    if hash_table[i] != '':
        f.write(f'{i}: ' + hash_table[i] + '\n')
f.close()

