#4963 섬의 개수
#가로/세로/대각선일 경우에 연결가능한 섬 - 섬의 갯수 세기
#DFS로 탐색하여 이미 탐색한 좌표에 visted 표기하고, 첫번째 탐색시에 count++

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, 0, -1, -1, -1]


def DFS(i, j):
	visited[i][j] = 1
	for l in range(9):
		ni = i + dy[l]
		nj = j + dx[l]
		if 0 <= ni < h and 0 <= nj < w:
			if bd[ni][nj] == 1 and visited[ni][nj] == 0:
				DFS(ni, nj)


while 1:
	# w h 입력받기
	w, h = map(int, input().split())
	if w == 0 and h == 0:
		break
	# 맵 입력
	bd = []
	for i in range(h):
		bd.append(list(map(int, input().split())))
	
	# 맵 탐색
	count = 0
	visited = [[0 for _ in range(w)] for k in range(h)]
	for i in range(h):
		for j in range(w):
			if bd[i][j] == 1 and visited[i][j] == 0:
				DFS(i, j)
				count += 1
	print(count)