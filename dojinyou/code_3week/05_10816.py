# https://www.acmicpc.net/problem/10816

from sys import stdin
input = stdin.readline

# binary search
def getLowerBound(array, value):
	low = 0
	high = len(array)
	while (low < high) :
		mid = (low+high)//2
		if value <=array[mid] :
			high = mid
		else :
			low = mid + 1
	return low

def getUpperBound(array, value):
	low = 0
	high = len(array)
	while (low < high):
		mid = (low+high)//2
		if value >= array[mid] :
			low = mid + 1
		else :
			high = mid
	return low

n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
for c in list(map(int, input().split())):
	print(getUpperBound(cards, c) - getLowerBound(cards,c), end=' ')

# dict
n = int(input())
cards = {}
for card in list(map(int, input().split())):
	if cards.get(c) :
		cards[card] += 1
	else :
		cards[card] = 1
m = int(input())
for c in list(map(int, input().split())):
	if cards.get(c) :
		print(cards[c], end=' ')
	else :
		print(0, end=' ')