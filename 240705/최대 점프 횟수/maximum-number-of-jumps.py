import sys
input = sys.stdin.readline

N = int(input())
jumps = list(map(int, input().split()))
dp = [-1 for i in range(N)]
dp[0] = 0
# if jumps[0] == 0:
#     print(0)
# else:
for idx in range(1, N):
    for prev in range(1, N+1):
        if idx - prev < 0:
            break
        if jumps[idx-prev] >= prev:
            if dp[idx-prev] == -1:
                continue
            dp[idx] = max(dp[idx], dp[idx-prev] + 1)
print(max(dp))