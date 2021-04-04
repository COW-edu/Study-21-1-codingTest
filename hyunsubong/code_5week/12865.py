# 평범한 배낭 

import sys
read = sys.stdin.readline

n, k = map(int, read().split())
items = [tuple(map(int, read().split())) for _ in range(n)]
bag = [0 for _ in range(k+1)]

for i in range(n):
    for j in range(k, 1, -1):
        if items[i][0] <= j:
            bag[j] = max(bag[j], bag[j-items[i][0]] + items[i][1])

print(bag[-1])