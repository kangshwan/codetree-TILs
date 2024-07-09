import sys
input = sys.stdin.readline

N = int(input())
infos = []
max_day = 0
for _ in range(N):
    s, e, p = map(int, input().split())
    infos.append((s,e,p))
    max_day = max(max_day, e)

dp = [0] * (max_day + 1)
idx = 0
for i in range(max_day + 1):
    dp[i] = dp[i-1]
    while idx < len(infos):
        s, e, p = infos[idx]
        if e != i:
            break
        dp[e] = max(dp[e], p + dp[s-1])
        idx += 1

print(dp[max_day])