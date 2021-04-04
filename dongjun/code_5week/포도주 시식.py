N = int(input())
arr = [0]
cache = [0 for _ in range(N + 1)]

for _ in range(N):
    arr.append(int(input()))

for i in range(1, N + 1):
    if i == 1:
        cache[1] = arr[1]
    elif i == 2:
        cache[2] = arr[1] + arr[2]
    else:
        cache[i] = max(cache[i-3] + arr[i-1] + arr[i],
                       cache[i-2] + arr[i], cache[i-1])

print(cache[N])
