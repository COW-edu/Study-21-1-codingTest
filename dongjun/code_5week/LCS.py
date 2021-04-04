a = list(input())
b = list(input())
cache = [[0]*(len(a)+1) for _ in range(len(b)+1)]
for i in range(1, len(cache)):
    for j in range(1, len(cache[i])):
        if b[i-1] == a[j-1]:
            cache[i][j] = cache[i-1][j-1] + 1
            continue
        cache[i][j] = max(cache[i-1][j], cache[i][j-1])
print(cache[-1][-1])
