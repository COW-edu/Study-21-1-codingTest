# https://www.acmicpc.net/problem/1463
# 1로 만들기

from sys import stdin
input = stdin.readline

i = int(input())
result = 3 ** i

def calc(x, n):
    global result

    if x == 1:
        if n < result:
            result = n
        return
    elif n >= result:
        return

    if x % 2 == 0:
        calc(x // 2, n + 1)
    if x % 3 == 0:
        calc(x // 3, n + 1)
    calc(x - 1, n + 1)

calc(i, 0)
print(result)
