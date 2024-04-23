N, K = map(int, input().split())
nums = list(map(int, input().split()))

# 각 숫자가 몇 번 나왔는지 기록
# in hash map

count = {}
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

ans = 0
# i가 고정되어있을 때, i 보다 작은 j와 i 보다 큰 k의 값을 hashmap으로 구현한다.

# 배열을 앞에서 부터 순회한다.
for i in range(N):
    # i는 이미 순회했다고 가정하기 때문에, count에서 i번째를 제거한다.
    count[nums[i]] -= 1
    
    for j in range(i):
        # j의 경우 i보다 작고, 이미 순회했다고 가정하며 count에서 제거되었을 것이다.
        # 그렇다면, k에서 nums[i]와 nums[j]를 뺀 값인 diff가 count에 존재한다면, 
        # count[diff]개의 diff가 i 보다 큰 k 인덱스들에 있다는 의미가 된다!
        diff = K - nums[i] - nums[j]
        if diff in count:
            ans += count[diff]

print (ans)