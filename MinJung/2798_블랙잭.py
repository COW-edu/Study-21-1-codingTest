nm = input("카드의 개수, M: ")
N, M = nm.split()
M3 = input("카드 정보: ")
M3=M3.split()
M3 = list(map(int,M3))
M3.sort()
if (M3[0]+M3[1]+M3[2]) > int(M):
    print("No Card")
else:
    sum = 0
    for i in range(0, int(N)-2):
        for j in range(i+1, int(N)-1):
            for x in range(j+1,int(N)):
                if M3[i]+M3[j]+M3[x] <= int(M):
                    if sum < M3[i]+M3[j]+M3[x]:
                        sum = M3[i]+M3[j]+M3[x]

    print(sum)


"""combinations"""