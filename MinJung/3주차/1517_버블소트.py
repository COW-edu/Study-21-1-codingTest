"""소 하드"""
import sys

def bubble_sort(arr):
    num=0
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                num+=1
    return num                
N = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
print(bubble_sort(l))