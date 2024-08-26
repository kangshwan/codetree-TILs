import sys
input = sys.stdin.readline
N, M = map(int, input().split())
coins = list(map(int, input().split()))
DP = [-1 for _ in range(10001)]
for coin in coins:
    DP[coin] = 1
for price in range(1, M+1):
    tmp = DP[price]
    for coin in coins:
        # price - coin >= 0 --> 현재 coin을 사용하여 price를 만들 수 있는지 확인
        # DP[price-coin] != -1 --> price가 price - coin일 때, 동전들을 사용하여 만들 수 있는 경우가 있는지 확인.
        # DP[price-coin] == -1이라는 뜻은, price가 price - coin일 때 동전들로 만들 수 없다는 뜻. 즉 현재 coin을 사용하여 price를 만들 수 없다!
        if price - coin >= 0 and DP[price-coin] != -1:
            # DP[coin]은 일정하게 1이다.
            # DP[price - coin]으로 만들 수 있기 때문에, + 1 을 더하고, 기존 값과 비교하여 더 큰지 확인한다.
            tmp = max(tmp, DP[coin]+DP[price-coin])
    DP[price] = tmp
print(DP[M])

'''
coin = 3
 0  1  2  3  4  5  6  7  8  9
[0, 0, 0, 1, 1, 1, 2, 2, 2, 3] ???
[0  0  0  1  0  0  2
'''