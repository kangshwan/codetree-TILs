N, K = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j] == K:
            ans += 1
print(ans)