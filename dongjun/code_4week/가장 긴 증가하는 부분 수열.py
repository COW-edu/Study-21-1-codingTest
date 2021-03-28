N = int(input())
arr = list(map(int, input().split()))
cache = [1]*N

for i in range(1, N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            cache[i] = max(cache[i], cache[j]+1)

print(max(cache))
