import sys
sys.stdin = open('input/9012.txt', 'r')


T = int(input())

for t in range(T):
    arr = list(input())
    stack = []
    result = 'YES'

    for a in arr:
        if a == '(':
            stack.append(a)
        else:
            if len(stack) == 0:
                result = 'NO'
            else:
                stack.pop()

    if result == 'YES':
        if len(stack) != 0:
            result = 'NO'
    print(result)
