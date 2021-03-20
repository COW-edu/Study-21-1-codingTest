# https://www.acmicpc.net/problem/2110
# 공유기 설치

from sys import stdin
input = stdin.readline

def compare(homes, distance):
    count = 1
    current = homes[0]

    for home in homes[1:]:
        if home - current >= distance:
            count += 1
            current = home

    return count

home, num = map(int, input().split())
homes = [int(input().rstrip()) for _ in range(home)]
homes.sort()

start = 1
end = homes[-1] - homes[0]
ans = None

while start <= end:
    mid = (start + end) // 2
    result = compare(homes, mid)

    if result >= num:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
