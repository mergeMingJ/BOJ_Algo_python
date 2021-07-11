import sys
sys.stdin = open('input/12847.txt', 'r')

# 슬라이딩 윈도우
# 매번 처리되는 중복된 요소를 버리지 않고 재사용함으로써 낭비되는 계산을 하지 않음으로써
# 효율적으로 처리하는 방법

n, m = map(int, input().split())
cost = list(map(int, input().split()))

window_sum = 0
sum_lst = []

start = 0
end = m

for i in range(n):
    window_sum += cost[i]
    if i > (end-1):
        end += 1
        window_sum -= cost[start]
        start += 1
    sum_lst.append(window_sum)

print(max(sum_lst))
