print('Введите строку')
seq = input()
checker = []
map = {')':'(', ']':'[', '}':'{'}
is_right = True
for i in range(len(seq)):
    if (seq[i] == ')') or (seq[i] == ']') or (seq[i] == '}'):
        if (len(checker) == 0) or (checker[-1] != map[seq[i]]):
            is_right = False
            break
        else:
            checker.pop()
    else:
        checker.append(seq[0])
if len(checker) != 0:
    is_right = False

if is_right:
    print('Строка правильная')
else:
    print('Строка неправильная')
