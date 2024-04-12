N, M = map(int, input().split())
nums = list(map(int, input().split()))
d = {}
for n in nums:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
queries = list(map(int, input().split()))
for q in queries:
    if q in d:
        print(d[q], end=' ')
    else:
        print(0, end=' ')