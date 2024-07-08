import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = 0
dp = [[0 for _ in range(N)] for _ in range(2)]
dp[0][0] = 1
dp[1][0] = 1
for i in range(1, N):
    inc = 0
    dec = 0
    for j in range(i, -1, -1):
        if arr[j] < arr[i]:
            inc = max(inc, dp[0][j])
        if arr[j] > arr[i]:
            dec = max(dec, max(dp[1][j], dp[0][j]))
    dp[0][i] = inc + 1
    dp[1][i] = dec + 1
answer = max(max(dp[0]), max(dp[1]))
print(answer)