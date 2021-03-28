# https://www.acmicpc.net/problem/11726
# 2xn 스타일링

from sys import stdin
input = stdin.readline

i = int(input())
l = [0, 1, 2] # 0, 2, 4

for n in range(3, i + 1):
    l.append(l[n - 1] + l[n - 2])

print(l[i] % 10007)
