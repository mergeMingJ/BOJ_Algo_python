import sys
sys.stdin = open('input/2504.txt', 'r')

string = list(input())


# 다시!!!!
stack = []

for char in string:
    if char == ')':
        if stack:
            while stack:
                pre = stack.pop(-1)
                if pre == '(':
                    stack.append(2)
                    break
                elif pre == '[':
                    break
                else:
                    stack.append(pre*2)
    elif char == ']':
        if stack:
            while stack:
                pre = stack.pop(-1)
                if pre == '[':
                    stack.append(3)
                    break
                elif pre == '(':
                    break
                else:
                    stack.append(pre*3)
    else:
        stack.append(char)

print(stack)
if '[' in stack or '(' in stack:
    print(0)
else:
    print(sum(stack))