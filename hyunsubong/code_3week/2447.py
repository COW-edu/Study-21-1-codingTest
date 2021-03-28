# 별 채우기

def pattern(k):
    matrix = []
    for i in range(3 * len(k)):
	    if i // len(k) == 1:
	        matrix.append(k[i % len(k)] + " " * len(k) + k[i % len(k)])
	    else:
	        matrix.append(k[i % len(k)] * 3)
    return(list(matrix))

n = int(input())
basic_matrix = ["***", "* *", "***"]
count = 0
while n != 3:
    n = n/3
    count += 1

for i in range(count):
    basic_matrix = pattern(basic_matrix)

for i in basic_matrix:
    print(i)