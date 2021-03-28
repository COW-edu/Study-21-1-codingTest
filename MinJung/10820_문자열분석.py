""" 입력 어캐 여러줄 받아여 ㅠㅠ"""
"""정규표현식 참고해보자"""
lines=[]
while(True):
    line = input()
    if line=="":
        break 
    else:
        lines.append(line)
for i in lines:
    so=0
    dae=0
    num=0
    str = list(i)
    blank = len(str)
    str=' '.join(str).split()
    blank-=len(str)
    for j in str:
        if j in '0123456789':
            num+=1
        elif ord(j)>=97 and ord(j)<=122:
            so+=1
        else: 
            dae+=1
    print(so, dae, num, blank)