N = int(input())
arr = list(map(int, input().split()))
cache = [0]*N
for i in range(N):
    cache[i] = max(cache[i-1]+arr[i], arr[i])

print(max(cache))
