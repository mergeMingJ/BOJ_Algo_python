import sys
sys.stdin = open('input/10866.txt', 'r')

# split()을 사용하면 List로 저장됨

N = int(sys.stdin.readline())
deque = []

for n in range(N):
    string = sys.stdin.readline()
    if ' ' in string:
        todo, x = string.split()
        x = int(x)

        # push_front X: 정수 X를 덱의 앞에 넣는다.
        if todo == 'push_front':
            deque.insert(0, x)
        # push_back X: 정수 X를 덱의 뒤에 넣는다.
        elif todo == 'push_back':
            deque.append(x)
    else:
        # split()을 사용하면 List로 저장됨
        [todo] = string.split()

        # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if todo == 'pop_front':
            if len(deque) == 0:
                print(-1)
            else:
                print(deque.pop(0))
        # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        elif todo == 'pop_back':
            if len(deque) == 0:
                print(-1)
            else:
                print(deque.pop(-1))
        # size: 덱에 들어있는 정수의 개수를 출력한다.
        elif todo == 'size':
            print(len(deque))
        # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
        elif todo == 'empty':
            if len(deque) == 0:
                print(1)
            else:
                print(0)
        # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        elif todo == 'front':
            if len(deque) == 0:
                print(-1)
            else:
                print(deque[0])
        # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        elif todo == 'back':
            if len(deque) == 0:
                print(-1)
            else:
                print(deque[-1])