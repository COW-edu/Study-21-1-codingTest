# https://www.acmicpc.net/problem/1654
# 랜선 자르기

from sys import stdin
input = stdin.readline

def cut_line(lines, length):
    return sum([x // length for x in lines])

line, num = map(int, input().split())
lines = [int(input().rstrip()) for _ in range(line)]

start = 1
end = max(lines)
ans = None

while start <= end:
    mid = (start + end) // 2
    result = cut_line(lines, mid)

    if result >= num:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
