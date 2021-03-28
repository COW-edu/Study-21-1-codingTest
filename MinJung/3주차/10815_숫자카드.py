import sys
from collections import defaultdict

N = int(sys.stdin.readline())
Nlist = map(int,sys.stdin.readline().split())
dic = defaultdict(int)
for i in Nlist:
    dic[i]=1
M = int(sys.stdin.readline())
Mlist = map(int,sys.stdin.readline().split())
for i in Mlist:
    print(dic[i], end=" ")
