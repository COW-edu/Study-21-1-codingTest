# https://www.acmicpc.net/problem/2805
# 나무 자르기

from sys import stdin
input = stdin.readline

def chop(nums, h):
    return sum([x - h for x in nums if x > h])

num, limit = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = max(nums)
ans = None

while start <= end:
    mid = (start + end) // 2
    result = chop(nums, mid)

    if result >= limit:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
