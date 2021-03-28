N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
cache = [0]*(N+1)

for i in range(N+1):
    if i == 0:
        continue
    elif i == 1:
        cache[i] = arr[i]
        continue
    elif i == 2:
        cache[i] = arr[i] + arr[i-1]
        continue
    cache[i] = arr[i] + max(arr[i-1]+cache[i-3], cache[i-2])
print(cache[N])
