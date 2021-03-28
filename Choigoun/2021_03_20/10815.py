
import sys

#집합이용하기
input() # 필요없음
n = set(map(int,sys.stdin.readline().split())) #입력받은 숫자들 집합 지정
input() # 필요없음
m = list(map(int,sys.stdin.readline().split()))

for i in m:
    if i in n: 
        print(1, end=' ')#end 통해서 줄바꿈 X

    else:
        print(0, end=' ')
