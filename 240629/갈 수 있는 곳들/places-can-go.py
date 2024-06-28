import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [-1,0,1,0]
answer = 0

N, K = map(int, input().split())
visited = [[False for _ in range(N)] for _ in range(N)]
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

def BFS(x, y):
    global answer
    if visited[x][y]:
        return;
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    answer += 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if inRange(nx, ny) and not visited[nx][ny] and not board[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                answer += 1


for _ in range(K):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    BFS(x, y)
print(answer)