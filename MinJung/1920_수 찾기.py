def binarySerach(target, l, left, right):
    while left<=right:
        mid = (left+right)//2
        if l[mid]>target:
            right=mid-1
        elif l[mid]<target:
            left = mid+1
        elif l[mid] == target:
            return 1
    return 0
    

N = int(input())
Nlist =  [int(x) for x in input().split()]
M = int(input())
Mlist = [int(x) for x in input().split()]
Nlist.sort()

for i in Mlist:
    print(binarySerach(i, Nlist, 0, N-1))


"""Dic은 O(1)이기 때문에 활용하면 좋다"""