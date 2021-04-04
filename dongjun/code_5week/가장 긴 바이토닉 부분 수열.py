def lis(arr):
    cache = [1]*len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[j]+1, cache[i])
    return cache


N = int(input())
arr = list(map(int, input().split()))
front = lis(arr)
arr.reverse()
back = lis(arr)
back.reverse()
res = [0]*N
for i in range(N):
    res[i] = front[i]+back[i]-1
print(max(res))
