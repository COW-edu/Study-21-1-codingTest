# https://www.acmicpc.net/problem/1012

from collections import deque
from sys import stdin
input = stdin.readline

def BFS(s):
	q = deque([s])
	while q :
		lx,ly = q.popleft()
		if adj[lx][ly] :
			adj[lx][ly] = 0
			for _ in range(4):
				if lx != 0 :
					q.append((lx-1, ly))
				if ly != 0 :
					q.append((lx, ly-1))
				if lx != m-1 :
					q.append((lx+1, ly))
				if ly != n-1 :
					q.append((lx, ly+1))
num = int(input())
for _ in range(num):
	m,n,k = map(int, input().split())
	adj = [[0]*n for _ in range(m)]
	locations = []
	cnt = 0
	for _ in range(k):
		x, y = map(int,input().split())
		adj[x][y] = 1
		locations.append((x,y))

	for lx,ly in locations :
		if adj[lx][ly] :
			BFS((lx,ly))
			cnt +=1
	print(cnt)