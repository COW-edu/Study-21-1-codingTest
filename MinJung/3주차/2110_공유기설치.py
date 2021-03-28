import sys
    
N, C = sys.stdin.readline().split()
l = []
for i in range(int(N)):
    l.append(int(sys.stdin.readline()))
l.sort()
start, end = 1, l[int(N)-1]-l[0]
while start<=end:
    mid = end+start//2
    AP = 1   
    check = l[0]
    for i in range(len(l)):
        if l[i]-check>=mid:
            check = l[i]
            AP+=1
    if AP >= int(C):
        start = mid +1
    elif AP < int(C):
        end = mid -1

print(end)