import sys

N, K = map(int,sys.stdin.readline().split())
WL = [0]*N
VL = [0]*N
maxW= [0]*N
maxV= [0]*N
for i in range(N):
    W, V = map(int,sys.stdin.readline().split())
    if W<K:
        WL[i], maxW[i] = W,W
        VL[i], maxV[i] = V,V
    for j in range(i):
        if W+WL[j]<=K and maxV[i]<VL[j]+V:
            maxW[i],maxV[i] = W+WL[j], VL[j]+V
        if maxW[j]+WL[i]<=K :
            maxW[i],maxV[i] = WL[j]+WL[i],VL[j]+V
print(max(maxV))
