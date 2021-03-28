import sys
N,M=map(int, sys.stdin.readline().split())
L=list(map(int, sys.stdin.readline().split()))
L+=list(map(int, sys.stdin.readline().split()))
L.sort()
for i in L:
    print(i,end=" ")
