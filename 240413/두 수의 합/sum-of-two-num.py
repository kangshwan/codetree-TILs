N, K = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
d = {}
cnt = {}
for idx, num in enumerate(nums):
    if num in cnt:
        cnt[num].append(idx)
    else:
        cnt[num] = [idx]
    
    if num not in d:
        d[num] = K-num

for idx, num in enumerate(nums):
    if K-num in d:
        tmp = 0
        for num in cnt[K-num]:
            if num > idx:
                tmp += 1
        ans += tmp
print(ans)