import sys
input = sys.stdin.readline

N = int(input())
sticks = list(map(int, input().split()))
DP = [[0 for _ in range(N)] for _ in range(N+1)]

for dist in range(1, N+1):
    DP[dist][0] = sticks[0]*dist

for s in range(1, N):
    for dist in range(1, N+1):
        # 길이보다 막대기가 길다면..
        if dist < s+1:
            DP[dist][s] = DP[dist][s-1]
        # 막대기를 추가할 수 있다면
        else:
            # 막대기 추가 X vs 막대기 추가, 이전 단계에서 s 추가 or 같은 s 추가
            DP[dist][s] = max(DP[dist][s-1], sticks[s] + max(DP[dist-(s+1)][s-1], DP[dist-(s+1)][s]))
print(DP[-1][-1])