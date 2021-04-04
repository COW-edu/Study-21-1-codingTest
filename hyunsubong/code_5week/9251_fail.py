# LCS

import sys
read = sys.stdin.readline

l1 = read().strip()
l2 = read().strip()

table = [[0] * (len(l1)+1) for _ in range(len(l2)+1)]

for i in range(1,len(l1)+1) :
  for j in range(1,len(l2)+1) :
    if l1[j-1] == l2[i-1] :
      table[i][j] = table[i-1][j-1] + 1
    else :
      table[i][j] = max(table[i][j-1], table[i-1][j])

print(table[-1][-1])