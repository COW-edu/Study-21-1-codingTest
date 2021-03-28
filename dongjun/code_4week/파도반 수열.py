cache = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
arr = []
for _ in range(int(input())):
    arr.append(int(input()))
if max(arr) > 10:
    for i in range(10, max(arr)+1):
        cache.append(cache[i-2]+cache[i-3])
for i in arr:
    print(cache[i-1])
