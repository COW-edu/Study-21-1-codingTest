# 피보나치 수

import sys

n = int(sys.stdin.readline())
l = [0 for i in range(n+2)]
l[1] = 1
for i in range(2, n+2) :
    l[i] = l[i-1] + l[i-2]
sys.stdout.write(str(l[i-1]))