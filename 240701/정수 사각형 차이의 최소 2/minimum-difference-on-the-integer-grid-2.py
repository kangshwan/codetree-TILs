import sys
input = sys.stdin.readline
N = int(input())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

def check():
    dp = [[10e9 for _ in range(N)] for _ in range(N)]
    dp[0][0] = board[0][0]

    for i in range(1,N):
        dp[i][0] = max(dp[i-1][0], board[i][0])
        dp[0][i] = max(dp[0][i-1], board[0][i])
        for j in range(1, N):
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), board[i][j])
    return dp[N-1][N-1]

# 숫자가 1~100이기 때문에, 최소값을 고정해가며 경로를 찾는다.

INF = 10e9
ans = 10e9
for low in range(1, 101):
    for i in range(N):
        for j in range(N):
            if board[i][j] < low:
                board[i][j] = INF

    max_val = check()
    if max_val == INF:
        continue
    ans = min(ans, max_val - low)

print(ans)