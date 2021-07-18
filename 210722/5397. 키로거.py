import sys
sys.stdin = open('input/5397.txt', 'r')

T = int(input())

for t in range(T):
    string = input()
    left = []
    right = []
    ans = ''
    i = 0
    for char in string:
        if char == '-':
            if len(left) != 0:
                left.pop(-1)
        elif char == '<':
            if len(left) != 0:
                num = left.pop(-1)
                right.append(num)
        elif char == '>':
            if len(right) != 0:
                num = right.pop(-1)
                left.append(num)
        else:
            left.append(char)

    left.extend(reversed(right))
    print(('').join(left))