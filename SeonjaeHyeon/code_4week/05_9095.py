# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기

from sys import stdin
input = stdin.readline

result = 0

def calc(x, t):
    global result

    if x == t:
        result += 1
        return
    elif x > t:
        return

    calc(x + 1, t)
    calc(x + 2, t)
    calc(x + 3, t)

n = [int(input()) for _ in range(int(input()))]

for i in n:
    calc(0, i)
    print(result)
    result = 0
