def fib(num):
    fiblist=[0,1]
    for i in range(num-1):
        fiblist.append(fiblist[i]+fiblist[i+1])
    return fiblist[num]
print(fib(int(input(""))))