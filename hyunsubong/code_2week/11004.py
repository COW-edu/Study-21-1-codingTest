# K번째 수
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	512 MB	32404	10336	6487	37.111%

# 문제
# 수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.

# 둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)

# 출력
# A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.

import sys

n,k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
l = sorted(l)
sys.stdout.write(str(l[k-1]))