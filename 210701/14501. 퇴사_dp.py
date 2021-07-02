import sys
sys.stdin = open('input/14501.txt', 'r')




N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.insert(0,[0,0])


