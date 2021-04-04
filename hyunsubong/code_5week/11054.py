# 가장 긴 바이토닉 수열 

n = int(input())
l = list(map(int,input().split()))
dp_up = [1] * (n+1)
dp_down = [1] * (n+1)

for i in range(n):
    for j in range(i):
        if l[i] > l[j]:
            dp_up[i] = max(dp_up[i], dp_up[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if l[i] > l[j]:
            dp_down[i] = max(dp_down[i], dp_down[j] + 1)

dp_temp = [0] * (n+1)
for i in range(n):
    dp_temp[i] = dp_up[i] + dp_down[i] -1 

print(max(dp_temp))