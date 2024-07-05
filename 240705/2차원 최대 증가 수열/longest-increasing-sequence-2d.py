import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[-1 for _ in range(M)]for _ in range(N)]
dp[0][0] = 1
for x in range(N):
    for y in range(M):
        if dp[x][y] != -1:
            for nx in range(x+1, N):
                for ny in range(y+1, N):
                    if board[nx][ny] > board[x][y]:
                        dp[nx][ny] = dp[x][y] + 1
ans = -1
for i in dp:
    ans = max(ans, max(i))
print(ans)