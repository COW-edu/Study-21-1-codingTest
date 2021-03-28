import sys

N, M = map(int, sys.stdin.readline().split())
Hlist= list(map(int, sys.stdin.readline().split()))

low, high = 1, max(Hlist)
while low<=high:
    mid = (low+high)//2
    new = list(filter(lambda x: x>mid, Hlist))
    treesum=sum(new)-(mid*len(new))  
    if treesum>=M:
        low = mid+1
    if treesum<M:
        high = mid-1
print(high)