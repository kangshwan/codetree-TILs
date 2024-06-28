import sys
input = sys.stdin.readline
N = int(input())
nums = [[]for _ in range(4)]
for i in range(4):
    nums[i] = list(map(int, input().split()))
ab = dict()
cd = dict()
for i in range(N):
    for j in range(N):
        sum_ab = nums[0][i]+nums[1][j]
        sum_cd = nums[2][i]+nums[3][j]
        if sum_ab not in ab:
            ab[sum_ab] = 1
        else:
            ab[sum_ab] += 1
        if sum_cd not in cd:
            cd[sum_cd] = 1
        else:
            cd[sum_cd] += 1
answer = 0
for k in ab:
    if -k in cd:
        answer += ab[k]*cd[-k]
print(answer)