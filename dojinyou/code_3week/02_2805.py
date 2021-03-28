# https://www.acmicpc.net/problem/2805

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

cut_low = 0
cut_high = max(trees)
result = 0
while cut_high >= cut_low:
    pivot = int((cut_low + cut_high) / 2)
    # pivot의 길이로 자를 수 있는 나무의 총 길이
    cut_tree = sum([x - pivot if x >= pivot else 0 for x in trees])
    # 비교
    if cut_tree >= M:
        cut_low = pivot + 1
        # 이 높이로 M이상의 나무를 자를 수 있고, 저장된 정답보다 크다면 이 높이로 정답을 업데이트
        if result < pivot: result = pivot
    elif cut_tree < M: cut_high = pivot - 1