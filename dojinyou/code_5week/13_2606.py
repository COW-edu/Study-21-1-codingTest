# https://www.acmicpc.net/problem/2606

from collections import deque
from sys import stdin
input = stdin.readline

def BFS(s):
	q = deque([s])
	while q :
		v = q.popleft()
		if not visited[v] :
			visited[v] = True
			for e in adj[v]:
				if not visited[e] :
					q.append(e)

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

visited = [False]*(n+1)
BFS(1)
print(sum(visited)-1)