# Z
import sys

def Z_graph(n, r, c):
    global count
    if n == 2:
        if r == R and c == C:
            print(count)
            return
        count += 1
        
        if r == R and c+1 ==C:
            print(count)
            return
        count += 1
        
        if r+1 == R and c+1 == C:
            print(count)
            return
        count += 1
        
        if r+1 == R and c+1 == C:
            print(count)
            return
        count += 1
        return
    Z_graph(n//2,r,c)
    Z_graph(n//2, r, c+n//2)
    Z_graph(n//2, r+n//2, c)
    Z_graph(n//2, r+n//2, c+n//2)    

N, R, C= map(int, sys.stdin.readline().split())
count = 0
Z_graph(2**N, 0,0)