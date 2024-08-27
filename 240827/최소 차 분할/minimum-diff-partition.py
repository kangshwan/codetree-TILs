import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
sum_nums = sum(nums)
DP = [[0 for _ in range(N)] for _ in range(sum_nums+1)]
answer = 10000000
for sum_val in range(1, sum_nums+1):
    if sum_val >= nums[0]:
        DP[sum_val][0] = nums[0]
        answer = min(answer, abs(sum_nums-nums[0] - nums[0]))

for idx in range(1, N):
    num = nums[idx]
    for sum_val in range(1, sum_nums+1):
        if sum_val >= num:
            DP[sum_val][idx] = max(DP[sum_val][idx-1], DP[sum_val-num][idx-1] + num)
            answer = min(answer, abs(sum_nums-DP[sum_val][idx] - DP[sum_val][idx]))
print(answer)