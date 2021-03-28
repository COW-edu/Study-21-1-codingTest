"""내장함수 dequeue를 활용해보자 collections"""
num = int(input(""))
for i in range(num):
    N_M = input("")
    N, M = N_M.split()
    N = int(N)
    M = int(M)
    test_case = input("")
    test_case=test_case.split()
    test_case = list(map(int,test_case))
    test_num = 0
    while True:
        TF =True
        if N ==1:
            print("1")
            break
        for i in range(1,len(test_case)):
            if test_case[0] < test_case[i]:
                if M == 0:
                    M+=len(test_case)-1
                else:
                    M-=1
                first = test_case.pop(0)
                test_case.append(first)
                TF = False
                break
        if TF == True:
            test_case.pop(0)
            test_num+=1
            M-=1
        if M== -1:
            print(test_num)
            break
        if test_case == []:
            break


