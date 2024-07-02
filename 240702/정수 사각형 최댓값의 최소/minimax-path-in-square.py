import sys
input = sys.stdin.readline

N = int(input())
board=[]
for _ in range(N):
    board.append(list(map(int, input().split())))
dp = [[0 for _ in range(N)] for _ in range(N)]

dp[0][0] = board[0][0]
for i in range(1, N):
    dp[i][0] = max(dp[i-1][0], board[i][0])
    dp[0][i] = max(dp[0][i-1], board[0][i])

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), board[i][j])

print(dp[N-1][N-1])