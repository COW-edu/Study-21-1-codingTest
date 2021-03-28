from collections import defaultdict
import sys

d = defaultdict(list)
N = int(sys.stdin.readline())
for i in range(N):
    l=sys.stdin.readline().split()
    d[int(l[0])].append(int(l[1]))
    d[int(l[0])].sort()
newd = list(d.keys())
newd.sort()
for i in newd:
    for j in d[i]:
        print(i,j)
