# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열

from sys import stdin
input = stdin.readline

n = int(input())
nums = [int(x) for x in input().split()]

# https://github.com/MJU-Coin/Study-21-1-codingTest/issues/37
result = [1] * n
for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j] and result[i] < result[j] + 1:
            result[i] = result[j] + 1

print(max(result))
