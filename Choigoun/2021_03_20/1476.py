
import sys

E = 1
S = 1
M = 1
cnt = 1

A , B , C = map(int,sys.stdin.readline().split())

while(True): #1씩 증가시킨다. 
    if A==E and B==S and C==M :
        break # 입력받은 년도가 된다면 break
    E+=1 
    S+=1 
    M+=1
    cnt+=1
    if E>=16 : # 각각의 범위를 넘어가면 뺀다.
        E-=15
    if S>=29 : 
        S-=28
    if M>=20 : 
        M-=19



print(cnt)