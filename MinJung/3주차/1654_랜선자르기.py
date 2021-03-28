def binary_search(high, K, L):
    low= 0
    while low <= high:
        mid = (low + high) // 2
        newK = 0
        for i in L:
            newK+=i//mid
        if newK >=K:
            low = mid + 1
        if newK<K :
            high = mid - 1
    return high
N, K = map(int, input().split())
L=[]
for i in range(N):
    L.append(int(input()))
print(binary_search(max(L), K, L))
