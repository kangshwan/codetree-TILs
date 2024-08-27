import sys
input = sys.stdin.readline
N, M = map(int, input().split())
jewels = []
for _ in range(N):
    w, v = map(int, input().split())
    jewels.append((w, v))

DP = [0] * (M+1)

for max_weight in range(1, M+1):
    for jewel_idx in range(N):
        jewel_weight, jewel_value = jewels[jewel_idx]
        if max_weight >= jewel_weight:
            DP[max_weight] = max(DP[max_weight], jewel_value + DP[max_weight - jewel_weight])
print(DP[-1])