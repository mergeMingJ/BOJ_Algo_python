N = 5
circular_queue = [None] * N
global start
start = 0
global tail
tail = 0


def enQueue(x):
    global tail
    if tail == N:
        tail = 0
    circular_queue[tail] = x
    tail += 1
    print(circular_queue)
    return circular_queue

def Rear():
    print(circular_queue[tail-1])
    return circular_queue[tail-1]


def isFull():
    if circular_queue is not None:
        print(False)
    else:
        print(True)

def deQueue():
    global start
    circular_queue[start] = None
    if start == N - 1:
        start = 0
    else:
        start += 1

def Front():
    print(circular_queue[start])
    return circular_queue[start]


enQueue(10)
enQueue(20)
enQueue(30)
enQueue(40)
Rear()
isFull()
deQueue()
deQueue()
enQueue(50)
enQueue(60)
Rear()
Front()
