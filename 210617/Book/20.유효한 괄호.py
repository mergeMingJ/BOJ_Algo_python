inputs = '()[]{}'

stacks = list(('').join(inputs))

new = []

for stack in stacks:
    if stack == '(':
        new.append(stack)
    elif stack == ')' and new[-1] == '(':
        new.pop()
    if stack == '{':
        new.append(stack)
    elif stack == '}' and new[-1] == '{':
        new.pop()
    if stack == '[':
        new.append(stack)
    elif stack == ']' and new[-1] == '[':
        new.pop()
if len(new) == 0:
    result = 'true';
else:
    result = 'false'

print(result)
