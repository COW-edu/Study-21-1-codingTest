import sys
l=[0]*10001
N=int(sys.stdin.readline())
for i in range(N):
    l[int(sys.stdin.readline())]+=1
for i in range(len(l)):
    for j in range(l[i]):
        print(i)