import sys
sys.stdin = open('input/10799.txt', 'r')

bar = list(input())
cnt = 1
stack = []
flag = 0

for i in range(len(bar)-1):
    if bar[i] == '(':
        stack.append('(')
        if bar[i+1] == ')':
            flag = 1
            stack.pop(-1)
            if len(stack) != 0:
                cnt += len(stack)
    elif flag == 1:
        flag = 0
        continue
    elif bar[i] == ')':
        cnt += 1
        stack.pop(-1)
print(cnt)



