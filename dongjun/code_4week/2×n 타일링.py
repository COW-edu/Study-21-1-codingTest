N = int(input())
cache = [0]*(N+1)

for i in range(N+1):
    if i == 0 or i == 1:
        cache[i] = 1
        continue
    cache[i] = cache[i-1]+cache[i-2]
    cache[i] %= 10007

print(cache[N])
