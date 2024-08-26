import sys
input = sys.stdin.readline
N, M = map(int, input().split())
jewels = []
for _ in range(N):
    jewels.append(tuple(map(int, input().split())))
DP = [[0 for _ in range(M+1)] for _ in range(N)]

for weight in range(1, M+1):
    if weight >= jewels[0][0]:
        DP[0][weight] = jewels[0][1]

for idx in range(1, N):
    j_w, j_v = jewels[idx]
    for weight in range(1, M+1):
        # 무게를 초과하여 담을 수 없는 경우
        if weight - j_w < 0:
            DP[idx][weight] = DP[idx-1][weight]
        else:
            DP[idx][weight] = max(DP[idx-1][weight], j_v + DP[idx-1][weight-j_w])
print(DP[-1][-1])
'''
dp[i][j] : i번째 쥬얼의 순서일 때, 무게가 j인 경우의 최대 가치
'''