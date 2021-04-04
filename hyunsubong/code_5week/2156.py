# 포도주 시식

import sys
read = sys.stdin.readline

n = int(read())
l = [0]
inputs = [int(read()) for _ in range(n)]
l.extend(inputs)
dp = [0] * (n+1)
dp[1] = l[1]
if n > 1:
    dp[2] = l[1] + l[2]
for i in range(3, n+1):
    dp[i] = max(l[i] + dp[i-2], l[i] + l[i-1] + dp[i-3], dp[i-1])

print(dp[n])