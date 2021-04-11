# https://www.acmicpc.net/problem/9251

from sys import stdin
input = stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()
dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]

for i in range(1,len(word1)+1):
    for j in range(1,len(word2)+1):
        if word1[i-1] == word2[j-1] :
            dp[i][j] = dp[i-1][j-1]+1
        else :
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])