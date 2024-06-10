#include <iostream>
#define MAX_N 1000
#define MOD 10007

using namespace std;

int N;
int DP[MAX_N+1] = {0,1,2,};

int main() {
    cin >> N;
    for(int i = 3 ; i <= N ; i++){
        DP[i] = (DP[i-1] + DP[i-2]) % MOD;
    }
    cout << DP[N];
    return 0;
}
/*
N = 0일때 가지 수 : 0
N = 1일때 가지 수 : 1
N = 2일때 가지 수 : 2
N = 3일때 가지 수 : 3
N=0, 0
N=1, I
N=2, =, II.
사각형 채우기 방법은 가로로 2줄을 쌓아 2칸을 잡아먹거나, 세로로 1줄을 쌓는 두 가지 방법만 존재함.
N=2인 경우, N=1에서 I 하나를 쌓는 방법 + N=0에서 =, 가로 두 줄을 쌓는 방법 두 가지가 합쳐 총 2가지.
따라서 점화식 설계는 다음과 같다.
DP[N] = DP[N-1] + DP[N-2], N >= 3

*/