# 이해 안가

from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    time = 0
    truck = 0
    while len(bridge) != 0:
        out = bridge.popleft()
        truck -= out
        time += 1
        if truck_weights:
            if truck + truck_weights[0] <= weight:
                left = truck_weights.popleft()
                truck += left
                bridge.append(left)
            else:
                bridge.append(0)
    return time

print(8, solution(2, 10, [7, 4, 5, 6]))
print(10, solution(4, 2, [1, 1, 1, 1]))
print(101, solution(100, 100, [10]))
print(110, solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
print(4, solution(1, 1, [1, 1, 1]))
print(4, solution(1, 2, [1, 1, 1]))
print(6, solution(3, 3, [1, 1, 1]))
print(10, solution(3, 1, [1, 1, 1]))
print(14, solution(5, 5, [1, 1, 1, 1, 1, 2, 2]))
print(18, solution(7, 7, [1, 1, 1, 1, 1, 3, 3]))
print(19, solution(5, 5, [1, 1, 1, 1, 1, 2, 2, 2, 2]))
print(19, solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))
