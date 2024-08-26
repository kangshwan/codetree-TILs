import sys
input = sys.stdin.readline
N, M = map(int, input().split())
coins = list(map(int, input().split()))
DP = [-1 for _ in range(10001)]
for coin in coins:
    DP[coin] = 1
for price in range(1, M+1):
    # DP[i] = max(DP[i-c_1]+DP[c_1], DP[i-c_2]+DP[c_2], ... , DP[i-c_N]) + 1
    tmp = DP[price]
    for coin in coins:
        if price - coin >= 0 and DP[price-coin] != -1:
            tmp = max(tmp, DP[coin]+DP[price-coin])
    DP[price] = tmp
print(DP[M])

'''
coin = 3
 0  1  2  3  4  5  6  7  8  9
[0, 0, 0, 1, 1, 1, 2, 2, 2, 3] ???
[0  0  0  1  0  0  2
'''