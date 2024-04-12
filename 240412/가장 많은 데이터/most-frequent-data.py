N = int(input())
d = {}
for _ in range(N):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
print(max(d.values()))