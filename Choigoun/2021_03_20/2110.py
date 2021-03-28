
import sys

n,c = map(int,sys.stdin.readline().split()) # input

house = [] # house list append
for _ in range(n):
    x = int(input())
    house.append(x)

house.sort() # 오름차순 정렬

# 가장 낮은 좌표와 그 다음으로 낮은 좌표의 차이
start = house[1] - house[0]
# 가장 높은 좌표와 가장 낮은 좌표의 차이
end = house[-1] - house[0]

result = 0

while (start <= end):
    mid = (start+end)//2 # 해당 gap
    left = house[0] 
    count = 1 # 가능한 집의 개수

    for i in range(1, len(house)): #각각의 집 for문
        # left와의 거리가 mid 이상이면 count 증가
        if house[i] >= left+mid: # gap 이상
            count += 1
            left = house[i] #left를 그다음 집으로 
    
    if count >=c: #집이 공유기 개수보다 크면
        start = mid + 1
        result = mid # result값은 최대 거리가 된다
    else:
        end = mid - 1

print(result)

#참고
#https://assaeunji.github.io/python/2020-05-07-bj2110/