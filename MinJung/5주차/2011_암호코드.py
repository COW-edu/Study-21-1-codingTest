# 0 처리를 못함
import sys
from functools import reduce

num = sys.stdin.readline()
result = len(num)-2
new = 1
for i in range(len(num)-2):
    if int(num[i:i+2])>26:
        result-=1

for i in range(1, result+1):
    new *= i

if int(num)==0:
    print(0)
elif len(num)==1:
    print(1)
else:
    print(new%1000000)

