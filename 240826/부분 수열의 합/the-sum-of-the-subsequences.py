import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
DP = [[0 for _ in range(10001)] for _ in range(101)]
val_to_idx = {}
for i in range(N):
    DP[i][A[i]] = 1
    val_to_idx[A[i]] = i

# 수열 A에 대해서, 각 수열을 앞에서 부터 순회한다
for i in range(N):
    cur_a = A[i]
    for j in range(M+1):
        if j-cur_a > 0: 
            for idx in range(i): 
                DP[val_to_idx[cur_a]][j] = DP[val_to_idx[cur_a]][j] or DP[idx][j-cur_a]
        # DP[i-cur_a][i-cur_a]
# print(0, [i for i in range(M+1)])
# for i in A:
#     print(i, DP[val_to_idx[i]][:M+1])
if DP[val_to_idx[A[-1]]][M]:
    print("Yes")
else:
    print("No")
'''
0  1  2  3  4  5  6  7  8  9 10 11 12
0  1  1  1  1  1  1        1
이 방법으로는 안될것 같다... 다른 방법 생각!

DP[i] 는 합이 i인 부분수열이 있다면 1 없다면 0 ?
2중 DP로 만들어 보는건 어떤가?
DP[i][j] --> 숫자 i를 사용해서 j를 만들 수 있는지 체크.
a ==> i: 2, j: 7 DP[2][2] and DP[7-2][7-2] ==> 1
b ==> i: 4, j: 6 DP[4][4] and DP[6-4][6-4] ==> 1
c ==> DP[4][4] and DP[9-4][9-4] ==> 1
d ==> DP[9][9] and DP[11-9][11-9] ==> 1
e ==> DP[1][1] and DP[3-1][3-1] ==> 1
f ==> DP[1][1] and DP[8-1][8-1] ==> 1?
                   DP[2][8-1] ==> 1

  0  1  2  3  4  5  6  7  8  9 10 11 12
5    0  0  0  0  1  0  0  0  0  0  0  0  
2    0  1  0  0  0  0  a  0  0  0  0  0
4    0  0  0  1  0  b  0  0  c  0  0  0
9    0  0  0  0  0  0  0  0  1  0  d  0
1    1  0  e  0  1  1  1  f  0  1  0  1
'''