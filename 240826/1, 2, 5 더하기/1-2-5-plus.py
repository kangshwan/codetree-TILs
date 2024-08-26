import sys
input = sys.stdin.readline
N = int(input())
DP = [0 for _ in range(1001)]
DP[0] = 1

for n in range(1, N+1):
    tmp = 0
    for num in [1, 2, 5]:
        if n-num >= 0:
            tmp += DP[n-num]
    DP[n] = tmp%10007
print(DP[N])