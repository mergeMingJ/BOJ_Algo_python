import sys
sys.stdin = open('input/1780.txt', 'r')

N = int(input())
arr = [[int(a) for a in input().split()] for _ in range(N)]
check = {-1: 0, 0: 0, 1: 0}

