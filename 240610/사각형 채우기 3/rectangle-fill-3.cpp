#include <iostream>
#define MAX_N 1000
#define MOD 1000000007

using namespace std;

int N;
int DP[MAX_N+1] = {1, 2, 7,};
int main() {
    cin >> N;
    for(int i = 3 ; i <= N ; i++){
        for(int j = 1 ; j <= i ; j++){
            DP[i] += (DP[i-j]*2) % MOD;
            DP[i] %= MOD;
        }
        DP[i] += DP[i-2] % MOD;
        DP[i] %= MOD;
    }
    cout << DP[N];
    return 0;
}

/*
세로로 채우냐, 가로로 채우냐 문제.
세로로 채울 경우, 쪼갤 수 있는 경우의 수가 2가지. 긴거 하나 or 작은거 2개
가로로 채울 경우(2칸), 가능한 경우의 수 =, ㅁㅁㅡ, ㅡㅁㅁ, ㅁㅁㅁㅁ 4가지.

DP[N] = DP[N-1]*2 + DP[N-2]*3 +  + DP[N-3]
DP[2] = 7
DP[3] = DP[2]*2 + DP[1]*3 + DP[0]*2 = 7*2+2*3+1*2 = 14+6+2 = 22
DP[4] = DP[3]*2 + DP[2]*3 + DP[1]*2 + DP[0]*2 = 22*2 + 7*3 + 2*2 = 44 + 21 + 4 + 2= 71
DP[5] = DP[4]*2 + DP[3]*3 + DP[2]*2 + DP[1]*2 + DP[0]*2 = 71*2 + 22*3 + 7*2 + 2*2 + 2 = 142 + 66 + 14 + 4 + 2 = 228!
이왜진;
*/