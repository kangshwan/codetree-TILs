import sys
input = sys.stdin.readline

N = int(input())
lines = []
for _ in range(N):
    lines.append(tuple(map(int, input().split())))
lines.sort(key=lambda x: x[1])
lines.sort()
# dp[i]는 i번째 막대를 선택 or 선택하지 않는 경우 가장 많이 고른 개수
# 정렬을 이미 한번 진행했기 때문에, 중복됐다면 이전 막대들을 확인하여 최대를 찾는다.
dp = [0 for _ in range(N)]
dp[0] = 1
def dup(line1, line2):
    s1,e1 = line1
    s2,e2 = line2
    if s1 < s2 and e1 < e2:
        return False
    elif s1 > s2 and e1 > e2:
        return False
    return True

for idx in range(1, N):
    for prev in range(idx):
        if not dup(lines[idx], lines[prev]):
            dp[idx] = max(dp[idx], dp[prev] + 1)
print(max(dp))