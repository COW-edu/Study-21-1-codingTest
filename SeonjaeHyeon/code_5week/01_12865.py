# https://www.acmicpc.net/problem/12865
# 평범한 배낭

from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight = T[i - 1][0]
    value = T[i - 1][1]

    for j in range(1, K + 1):
        dp[i][j] = dp[i - 1][j]
        
        if j >= weight:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[N][K])
