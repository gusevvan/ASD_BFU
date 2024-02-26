P = 31
R = 2**31 - 1


def hash(string):
    cur_coef = 1
    result = 0
    for i in range(len(string) - 1, -1, -1):
        result += (ord(string[i]) - 96) * cur_coef
        result %= R
        cur_coef *= P
        cur_coef %= R
    return result


f = open('input.txt', 'r')
s = f.read()
s += ''
t = input()
hashS = hash(s[:len(t)])
hashT = hash(t)
answer = []
coef = 1
for i in range(len(t)):
    coef *= P
    coef %= R
for i in range(len(s) - len(t) + 1):
    if hashS == hashT:
        answer.append(i)
    if i < len(s) - len(t):
        hashS = (P * hashS - coef * (ord(s[i]) - 96) + ord(s[i + len(t)]) - 96) % R
print(answer)
