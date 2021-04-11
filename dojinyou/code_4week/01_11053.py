# https://www.acmicpc.net/problem/11053

from sys import stdin
input = stdin.readline

n = int(input())
num = list(map(int,input().split()))
dp = [1 for _ in range(n+1)]
# dp[i] = i번째 원소가 수열의 마지막인 최대 증가 수열의 길이값
for i in range(2,n+1):
    for j in range(1,i):
        if (num[j-1] < num[i-1]) and (dp[j]+1 > dp[i]) :
            dp[i] = dp[j]+1
print(max(dp))