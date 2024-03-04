def preBmBc(x):
    table = [len(x)] * 26
    for i in range(0, len(x) - 1):
        table[ord(x[i]) - 97] = len(x) - 1 - i
    return table


def isPrefix(x, p):
    j = 0
    for i in range(p, len(x)):
        if x[i] != x[j]:
            return False
        j += 1
    return True


def suffixLength(x, p):
    length = 0
    i = p
    j = len(x) - 1
    while i >= 0 and x[i] == x[j]:
        length += 1
        i -= 1
        j -= 1
    return length


def preBmGs(x):
    table = [0] * len(x)
    lastPrefixPosition = len(x)
    for i in range(len(x) - 1, -1, -1):
        if isPrefix(x, i + 1):
            lastPrefixPosition = i + 1
        table[len(x) - i - 1] = lastPrefixPosition - i + len(x) - 1
    for i in range(0, len(x) - 1):
        slen = suffixLength(x, i)
        table[slen] = len(x) - 1 - i + slen
    return table

def BM(y, x):
    answer = []
    if len(x) == 0:
        answer.append(-1)
        return answer
    bmBc = preBmBc(x)
    bmGs = preBmGs(x)

    i = len(x) - 1
    while i < len(y):
        j = len(x) - 1
        while x[j] == y[i]:
            if j == 0:
                answer.append(i)
                break
            i -= 1
            j -= 1
        i += max(bmGs[len(x) - 1 - j], bmBc[ord(y[i]) - 97])
    if len(answer) == 0:
        answer.append(-1)
    return answer


def main():
    y = input()
    x = input()
    print(BM(y, x))


main()
