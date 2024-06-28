import sys
from collections import defaultdict
df = defaultdict(int)
input = sys.stdin.readline
n, k = map(int, input().split())
nums = list(map(int, input().split()))
for num in nums:
    df[num] += 1

for k, v in sorted(sorted(df.items(),key = lambda x: x[0], reverse=True), key=lambda x : x[1], reverse=True)[:k]:
    print(k, end=' ')