# https://www.acmicpc.net/problem/2655

from sys import stdin
input = stdin.readline

n = int(input())
# i번째 벽돌이 가장 아래 있을 때의 최대 높이
height_tracking = [[0, []] for i in range(n+1)]
# block 정보 저장
blocks = [[0,0,0,0]]
for i in range(1,n+1):
    info = [i]
    info.extend(list(map(int, input().split())))
    blocks.append(info)
# 벽돌 밑면의 넓이, 벽돌의 높이 그리고 무게
b_map = {"number":0, "area":1, "height":2, "weight":3}
# 넓이를 기준으로 정렬
blocks.sort(key=lambda x:(x[b_map["area"]]))
for i in range(1,n+1):
    # 자신을 가장 아래 높을 때 값으로 초기화
    height_tracking[i][0] = blocks[i][b_map["height"]]
    height_tracking[i][1].append(blocks[i][b_map["number"]])
    # 자신보다 넓이가 작은 녀석들 탐색
    for j in range(1,i):
        # j가 자신보다 무게가 작다면
        if blocks[j][b_map["weight"]] < blocks[i][b_map["weight"]]:
            # j가 가장 아래인 높이에 i의 높이를 더한 것이 현재 i가 가장 아래일 때 최대 높이보다 크다면
            if height_tracking[j][0]+blocks[i][b_map["height"]] > height_tracking[i][0] :
                height_tracking[i][0] = height_tracking[j][0]+blocks[i][b_map["height"]]
                height_tracking[i][1] = height_tracking[j][1][:]
                height_tracking[i][1].append(blocks[i][b_map["number"]])
max_h = 0
max_tracking = []
for h, tracking in height_tracking :
    if max_h < h :
        max_h = h
        max_tracking = tracking
print(len(max_tracking))
for num in max_tracking :
    print(num)
