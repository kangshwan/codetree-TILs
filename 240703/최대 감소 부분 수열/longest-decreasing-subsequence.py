import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [1 for _ in range(N)]
for i in range(1, N):
    longest = 0
    for j in range(i, -1, -1):
        if nums[j] > nums[i]:
            longest = max(longest, dp[j])
    dp[i] = longest+1
ans = 1
for longest in dp:
    ans = max(ans, longest)
print(ans)