N, M = map(int, input().split())
d = {}
for idx, _ in enumerate(range(N)):
    s = input()
    d[str(idx+1)] = s
    d[s] = str(idx+1)
for _ in range(M):
    print(d[input()])