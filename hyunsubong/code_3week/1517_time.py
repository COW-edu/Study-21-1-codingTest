# 버블 소트

def merge(left, right):
    global count
    l=list()
    i=0
    j=0
    while(i<len(left) and j<len(right)):
        if left[i]<=right[j]:
            l.append(left[i])
            i+=1
        else :
            l.append(right[j])
            j+=1
    if i==len(left): 
        l = l + right[j:len(right)]
        count += 1
    if j == len(right): 
        l = l + left[i:len(left)]
        count += 1
    return l
 
def merge_sort(l):
    if len(l) <= 1: 
        return l
    m = len(l)//2
    left = merge_sort(l[:m])
    right = merge_sort(l[m:len(l)])
    return merge(left, right)

count = 1
input()
l = list(map(int, input().split()))
merge_sort(l)
print(count)