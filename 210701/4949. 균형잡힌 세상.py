import sys
sys.stdin = open('input/4949.txt', 'r')


while True:
    result = 'yes'
    string = input()
    stack = []

    if string == '.':
        break
    else:
        for char in string:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if len(stack) == 0:
                    result = 'no'
                    break
                else:
                    new = stack.pop(-1)
                    if new != '(':
                        result = 'no'
                        break
            elif char == '[':
                stack.append(char)
            elif char == ']':
                if len(stack) == 0:
                    result = 'no'
                    break
                else:
                    new = stack.pop(-1)
                    if new != '[':
                        result = 'no'
                        break
        if len(stack) != 0:
            result = 'no'
        print(result)

