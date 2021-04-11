# https://www.acmicpc.net/problem/11052

from sys import stdin
input = stdin.readline

n = int(input())
prices = [0]
prices.extend(list(map(int,input().split())))
dp = [price for price in prices]

for i in range(2,n+1):
    for j in range(i//2+1):
        dp[i] = max(dp[i], dp[j]+dp[i-j])
print(dp[n])