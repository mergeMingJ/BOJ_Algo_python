import sys
sys.stdin = open('input/4796.txt', 'r')

t = 1

while True:
    L, P, V = list(map(int, input().split()))
    if [L,P,V] == [0,0,0]:
        break
    n = V//P
    gap = V-(P*n)
    # 휴가의 나머지 날이 L보다 클 경우
    if gap > L:
        result = (L*n)+L
    else:
        result = (L*n)+gap
    print('Case {}:'.format(t), result)
    t+=1