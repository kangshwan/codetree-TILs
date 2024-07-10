import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
dp = [101] * (M+1)
dp[0] = 0
for num in A:
    for i in range(M, num-1, -1):
        dp[i] = min(dp[i-num]+1, dp[i])
if dp[M] == 101:
    print(-1)
else:
    print(dp[M])