# 9184 신나는 함수 실행
# 재귀함수 w(a, b, c)가 이미 구현되어 있음
# w가 새로운 함수로 분기되는 경우의 수가 너무 많기 때문에 이를 미리 기록하고, 탐색하는 다이나믹 프로그래밍을 접목해야함

import sys
input = sys.stdin.readline

def w(a, b, c):
	if a <= 0 or b <= 0 or c <= 0:
		return 1
	if dp[a][b][c] != 0:
		return dp[a][b][c]	
	if a > 20 or b > 20 or c > 20:
		return 1048576
	if a < b and b < c:
		return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
	return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


dp = [[[0 for i in range(51)] for j in range(51)] for k in range(51)]
for i in range(51):
	for j in range(51):
		for k in range(51):
			dp[i][j][k] = w(i, j, k)

while 1:
	a, b, c = map(int, input().split())
	if a == -1 and b == -1 and c == -1:
		break
	if a <= 0 or b <= 0 or c <= 0:
		print("w({}, {}, {}) = {}".format(a, b, c, 1))
	else:
		print("w({}, {}, {}) = {}".format(a, b, c, dp[a][b][c]))