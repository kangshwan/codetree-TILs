import sys
input = sys.stdin.readline
N = int(input())
board = []
dp = [[() for _ in range(N)] for _ in range(N)]

for _ in range(N):
    board.append(list(map(int, input().split())))

lowerbound = 3

def find_max_min(before, num):
    global lowerbound
    max_n, min_n = before
    if min_n <= num <= max_n:
        if min_n > lowerbound:
            lowerbound = min_n
        return before
    elif num < min_n:
        return (max_n, num)
    else:
        return (num, min_n)

dp[0][0] = (board[0][0], board[0][0])
for i in range(1, N):
    dp[0][i] = find_max_min(dp[0][i-1], board[0][i])
    dp[i][0] = find_max_min(dp[i-1][0], board[i][0])

for i in range(1,N):
    for j in range(1, N):
        board_num = board[i][j]
        upper = find_max_min(dp[i-1][j], board_num)
        left = find_max_min(dp[i][j-1], board_num)
        # 최대값이 작을수록 유리
        if upper[0] < left[0]:
            dp[i][j] = upper
            lowerbound = upper[1]
        elif left[0] < upper[0]:
            dp[i][j] = left
            lowerbound = left[1]
        else:
            # 최대값이 동일하다면, 최소값이 클수록 유리
            if upper[1] > left[1]:
                dp[i][j] = upper
                lowerbound = upper[1]
            else:
                dp[i][j] = left
                lowerbound = left[1]

def calc_diff(data):
    return data[0] - data[1]

print(calc_diff(dp[N-1][N-1]))