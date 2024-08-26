import sys
input = sys.stdin.readline
N, M = map(int, input().split())
coins = list(map(int, input().split()))
DP = [-1 for _ in range(10001)]
for coin in coins:
    DP[coin] = 1
for price in range(max(coins)+1, M+1):
    tmp = -1
    for coin in coins:
        if price - coin > 0 and DP[price-coin] != -1:
            tmp = max(tmp, DP[coin]+DP[price-coin])
    DP[price] = tmp
# print(DP[:M+1])
if DP[M] == 0:
    print(-1)
else:
    print(DP[M])