# https://www.acmicpc.net/problem/1780
# 종이의 개수

from sys import stdin
input = stdin.readline

num = [0, 0, 0] # 0, 1, -1

def paper(m):
    L = len(m)

    if L in (1, m.count(m[0])):
        num[m[0]] += 1
        return

    N = int(L ** .5)
    for i in range(N // 3):
        for j in range(N // 3):
            tmp = []
            M = N // 3

            for k in range(M):
                tmp.extend(m[j*M + N*i*M + k*N : j*M+M + N*i*M + k*N])

            paper(tmp)

n = int(input())
matrix = []
for _ in range(n):
    for x in input().split():
        matrix.append(int(x))

paper(matrix)
print(num[-1])
print(num[0])
print(num[1])
