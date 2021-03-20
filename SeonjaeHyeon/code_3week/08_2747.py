# https://www.acmicpc.net/problem/2747
# 피보나치 수

from sys import stdin
input = stdin.readline

n = int(input())

if n < 2:
    print(n)
else:    
    before = 0
    current = 1
    for i in range(2, n + 1):
        tmp = current
        current += before
        before = tmp

    print(current)
