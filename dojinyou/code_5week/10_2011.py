# https://www.acmicpc.net/problem/2011

from sys import stdin
input = stdin.readline

c = input()
n = len(c)
isPrinted = False

if c[0] == "0" :
    print("0")
    isPrinted = True
elif n == 1:
    print("1")
    isPrinted = True
else :
    for i in range(1,n):
        if c[i] == "0" and c[i-1] != "2" and c[i-1] != "1":
            print("0")
            isPrinted = True
            break
if not isPrinted :
    mod = 1000000
    dp = [1]*n
    for i in range(1,n):
        if c[i]=="0" :
            dp[i] = dp[i-2]
        elif c[i-1] + c[i] <= "26" and c[i-1] != "0":
            dp[i] = dp[i-1] + dp[i-2]
        else :
            dp[i] = dp[i-1]
    print(dp[n-1] % mod) 