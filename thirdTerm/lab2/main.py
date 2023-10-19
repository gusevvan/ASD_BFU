import sys
def calculate(first, second, operand):
    if operand == '-':
        return first - second
    if operand == '+':
        return first + second
    if operand == '*':
        return first * second
    if operand == '/':
        return first / second

def step(numbers, operands):
    while len(operands) > 0 and operands[-1] != '(':
        arr = [numbers[-1]]
        i = -2
        while i + 2 > -len(operands) and operands[i + 1] == '/':
            arr.append(numbers[i])
            i -= 1
        result = arr[-1]
        if len(arr) > 1:
            for j in range(len(arr) - 2, -1, -1):
                numbers.pop()
                operands.pop()
                if arr[j] == 0:
                    print('Division by zero!')
                    sys.exit()
                else:
                    result /= arr[j]
        if len(operands) > 0 and operands[-1] != '(':
            first, second = numbers[-2], result
            numbers.pop()
            numbers[-1] = calculate(first, second, operands[-1])
            operands.pop()
        else:
            numbers[-1] = result

expr = input()
if expr[-1] != '=':
    print("Expression need's to ending =")
    sys.exit()
expr = expr[:-1]
numbers = []
operands = []
current_number = ''
for i in range(len(expr)):
    if expr[i].isdigit():
        current_number += expr[i]
    elif expr[i] in ['+', '-', '*', '/', '(', ')']:
        if len(current_number) != 0:
            numbers.append(int(current_number))
            if expr[i] == '-':
                current_number = '-'
            else:
                current_number = ''
        if expr[i] == '+' or expr[i] == '-':
            if len(operands) > 0 and (operands[-1] == '*' or operands[-1] == '/'):
                step(numbers, operands)
            operands.append('+')
        elif expr[i] == ')':
            step(numbers, operands)
            if len(operands) == 0 or operands[-1] != '(':
                print('expr')
            else:
                operands.pop()
        else:
            operands.append(expr[i])
if len(current_number) != 0:
    numbers.append(int(current_number))
step(numbers, operands)
print(numbers[0])
