import sys
comp_num = int(sys.stdin.readline())
network = int(sys.stdin.readline())
computer = [[]]*(comp_num+1)
print(computer)
for i in range(network):
    num1,num2 = map(int,sys.stdin.readline().split())
    if num2 in computer[num1]:
        pass
    else:
        computer[num1].append(num2)
    if num1 in computer[num2]:
        pass
    else:
        computer[num2].append(num1)
    print(computer)
print(computer)