# https://www.acmicpc.net/problem/1912
# 연속합

from sys import stdin
input = stdin.readline

n = int(input())
nums = [int(x) for x in input().split()]
result = nums[0]

for i in range(len(nums)):
    for j in range(i + 1, len(nums) + 1):
        tmp = sum(nums[i:j])
        if result < tmp:
            result = tmp

print(result)
