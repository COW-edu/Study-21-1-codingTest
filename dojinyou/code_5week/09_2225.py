# https://www.acmicpc.net/problem/2225

from sys import stdin
input = stdin.readline

n, k = map(int,input().split())
if k == 1:
    print(1)
else :
    mod = 1000000000
    dp = [[0]*(k+1)  for _ in range(n+1)]
    for i in range(1,k+1):
        dp[0][i] = 1
    for i in range(1,n+1):
        for j in range(1,k+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
    print(dp[n][k])