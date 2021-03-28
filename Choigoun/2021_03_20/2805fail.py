
import sys
#시간초과 
N, M = map(int,sys.stdin.readline().split()) # N 과 M에 각각 숫자 input
tree = list(map(int, input().split()))
start = 1
end = max(tree) 

while start <= end:
    mid = (start + end)//2

    tree_cut = 0 #자른 나무들의 합
    for i in tree:
        if i >=mid:
            tree_cut += i-mid
    
    if tree_cut >= M:
        start = mid + 1
    else:
        end = mid -1

print(end)
