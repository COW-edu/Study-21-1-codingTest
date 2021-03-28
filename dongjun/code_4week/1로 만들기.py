N = int(input())
cache = [1000001]*(N+1)
for i in range(N+1):
    if i == 0 or i == 1:
        cache[i] = 0
    elif i == 2 or i == 3:
        cache[i] = 1
    elif i % 2 == 0 and i % 3 == 0:
        cache[i] = 1+min(cache[i//2], cache[i//3], cache[i-1])
    elif i % 2 == 0:
        cache[i] = 1+min(cache[i//2], cache[i-1])
    elif i % 3 == 0:
        cache[i] = 1+min(cache[i//3], cache[i-1])
    else:
        cache[i] = 1 + cache[i-1]
print(cache[N])
