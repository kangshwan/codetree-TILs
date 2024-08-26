import sys
input = sys.stdin.readline
N, M = map(int, input().split())
coins = list(map(int, input().split()))
DP = [0 for _ in range(10001)]
for coin in coins:
    DP[coin] = 1
for price in range(max(coins), M+1):
    # DP[i] = max(DP[i-c_1]+DP[c_1], DP[i-c_2]+DP[c_2], ... , DP[i-c_N]) + 1
    tmp = 0
    for coin in coins:
        if price - coin > 0:
            tmp = max(tmp, DP[coin]+DP[price-coin])
    DP[price] = tmp
# print(DP[:M+1])
if DP[M] == 0:
    print(-1)
else:
    print(DP[M])