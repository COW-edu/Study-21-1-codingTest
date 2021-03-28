# https://www.acmicpc.net/problem/11727
# 2xn 스타일링 2

from sys import stdin
input = stdin.readline

i = int(input())
l = [0, 1, 3] # 0, 2, 4

for n in range(3, i + 1):
    l.append(l[n - 1] + l[n - 2] * 2)

print(l[i] % 10007)
