import sys
input = sys.stdin.readline

N = int(input())
infos = []
for _ in range(N):
    s, e, p = map(int, input().split())
    infos.append((s,e,p))
dp = [0] * len(infos)
dp[0] = infos[0][2]
for i in range(1, len(infos)):
    s, e, p = infos[i]
    max_able = 0
    for j in range(i):
        t_s, t_e, _ = infos[j]
        if t_e < s:
            max_able = max(max_able, dp[j])
    dp[i] = p + max_able
# print(dp)
print(max(dp))

# import sys
# input = sys.stdin.readline

# N = int(input())
# infos = []
# for _ in range(N):
#     s, e, p = map(int, input().split())
#     infos.append((s,e,p))
# dp = [[0 for _ in range(len(infos)] for _ in range(2)]
# dp[1][0] = infos[0][2]
# for i in range(1, len(infos)):
#     # i번째 일을 하지 않는 경우
#     dp[0][i] = max(dp[0][i-1], dp[1][i-1])
#     # i번째 일을 하는 경우
#     s, e, p = infos[i]
#     max_able = 0
#     for j in range(i):
#         t_s, t_e, _ = infos[j]
#         if t_e < s:
#             max_able = max(max_able, dp[j])
#     dp[i] = max(dp[i-1], p + max_able)
# print(dp)
# # print(max(dp))