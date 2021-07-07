def push(x):
    # 요소 x를 큐 마지막에 삽입한다.
    Q_input.append(x)
    return Q_input
def pop():
    # 큐 처음에 있는 요소를 제거한다.
    peek()
    Q_output.pop(-1)
    return Q_output

def peek():
    # 큐 처음에 있는 요소를 조회 한다.
    # output의 모든 요소를 pop 하기때문에 input에 그 후에 push 되는거 고려 하지 않아도 됨
    if len(Q_output) == 0:
        while Q_input:
            item = Q_input.pop(-1)
            Q_output.append(item)
    return Q_output[-1]

def empty():
    # 큐가 비어있는지 여부를 리턴
    if len(Q_output) != 0:
        print(False)
        return False
    else:
        print(True)
        return True


Q_input = []
Q_output = []

push(1)
push(2)
peek()
pop()
push(3)
peek()
empty()





