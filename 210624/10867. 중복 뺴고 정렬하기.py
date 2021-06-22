import sys
sys.stdin = open('input/10867.txt', 'r')

N = int(input())
n_lst = list(map(int, input().split()))

new_lst = sorted(set(n_lst))

for new in new_lst:
    print(new, end=" ")