# 합분해

n, k = map(int, input().split())
dp = [0] * (n+1)
dp[0] = 1 

for i in range(1, k+1):
    for j in range(1, n+1):
        dp[j] = dp[j] + dp[j-1]
print(dp[n] % 1000000000)