# 타일 채우기

n = int(input())
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 0 
# dp[2] = 3
# dp[3] = 0
# dp[4] = 11
# dp[5] = 0
# dp[6] = 41

for i in range(2, n+1):
    if i % 2:
        dp[i] = 0
    else:
        dp[i] += dp[i-2] * 3
        for j in range(0, i-2, 2):
            dp[i] += dp[j] * 2
print(dp[n])