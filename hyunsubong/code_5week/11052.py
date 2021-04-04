# 카드 구매하기 


n = int(input())
l = [0]
l += list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = l[1]
dp[2] = max(l[1] * 2, l[2])

for i in range(3, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + l[j])

print(dp[n])