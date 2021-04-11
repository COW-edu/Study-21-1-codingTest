import sys 
N = int(sys.stdin.readline()) 
A = list(map(int, sys.stdin.readline().split())) 
increase = [1 for _ in range(N)] 

for i in range(N): 
    for j in range(i): 
        if A[i] > A[j] and increase[i] < increase[j] + 1: 
            increase[i] = increase[j] + 1

