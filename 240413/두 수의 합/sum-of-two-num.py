N, K = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
d = {}
for num in nums:
    d[num] = K-num

for num in nums:
    if d[num] in d:
        ans += 1
print(ans//2)