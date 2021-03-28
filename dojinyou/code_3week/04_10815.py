# https://www.acmicpc.net/problem/10815

from sys import stdin
input = stdin.readline

# 정렬해서 찾기
def binarySearch(c):
	l = 0
	r = n - 1
	while l <= r :
		t = (r+l)//2
		if cards[t] == c :
			return 1
		elif cards[t] > c :
			r = t - 1
		else :
			l = t + 1
	return 0


n = int(input())
cards = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

cards.sort()
for c in check :
	print(binarySearch(c), end=' ')
	
# dict로 찾기
cards = {}
n = int(input())
for i in list(map(int, input().split())):
	cards[i] = 1
m = int(input())
for c in list(map(int, input().split())):
	if (cards.get(c)):
		print(cards[c], end=' ')
	else:
		print(0, end=' ')