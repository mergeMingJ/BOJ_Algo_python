import sys
sys.stdin = open('input/14503.txt', 'r')

N, M = list(map(int, input().split()))

r,c,d =list(map(int, input().split()))

arr = [[int(a) for a in input().split()] for _ in range(M)]

print(arr)




