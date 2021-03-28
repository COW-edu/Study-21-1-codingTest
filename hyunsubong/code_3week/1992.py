# 쿼드트리

import sys

def search(x, y, k):
    if(k == 1):
        return str(matrix[x][y])
    result = []
    for i in range(x, x + k): # 0 ~ 8
        for j in range(y, y + k): # 0 ~ 8
            if(matrix[i][j] != matrix[x][y]):
                result.append('(')
                result.extend(search(x, y, k//2))
                result.extend(search(x, y + k//2, k//2))
                result.extend(search(x + k//2, y, k//2))
                result.extend(search(x + k//2, y + k//2, k//2))
                result.append(')')
                
                return result
            
    return str(matrix[x][y])
    
n = sys.stdin.readline()
matrix = [list(map(int, input())) for _ in range(n)]
print(''.join(search(0, 0, n)))
