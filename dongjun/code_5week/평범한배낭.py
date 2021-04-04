N, K = map(int, input().split())
cache = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    W, V = map(int, input().split())
    for j in range(1, K+1):
        if j < W:
            cache[i][j] = cache[i-1][j]
        else:
            cache[i][j] = max(cache[i-1][j], cache[i-1][j-W]+V)
print(cache[N][K])
