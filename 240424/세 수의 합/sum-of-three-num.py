N, K = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if sums == K:
                answer += 1
print(answer)