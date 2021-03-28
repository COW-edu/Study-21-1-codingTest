# 배열 합치기

import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split())) + list(map(int, sys.stdin.readline().split()))
print(" ".join(map(str, sorted(l))))