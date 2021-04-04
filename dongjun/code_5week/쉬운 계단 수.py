N = int(input())
cache = [[0]*10 for _ in range(N+1)]
for i in range(1, N+1):
    if i == 1:
        cache[i] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        continue
    for j in range(10):
        if j == 0:
            cache[i][j] = cache[i-1][j+1]
            continue
        if j == 9:
            cache[i][j] = cache[i-1][j-1]
            continue
        cache[i][j] = cache[i-1][j-1]+cache[i-1][j+1]
print(sum(cache[N]) % 1000000000)
