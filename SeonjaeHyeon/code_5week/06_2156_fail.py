# https://www.acmicpc.net/problem/2156
# 포도주 시식

from sys import stdin
input = stdin.readline

n = int(input())

dp = [0 for _ in range(n)]
wine = [int(input()) for _ in range(n)]

dp[0] = wine[0]
if n > 1:
    dp[1] = wine[0] + wine[1]

for i in range(3, n):
    dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])

print(dp[n - 1])
