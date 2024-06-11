#include <iostream>
#define MAX_N 1000

using namespace std;

int DP[MAX_N+1] = {0,1,3,};
int N;
int main() {
    cin >> N;
    for(int i = 3 ; i <= N ; i++){
        DP[i] = DP[i-1] + DP[i-2]*2;
    }
    cout << DP[N];
    return 0;
}
/*
기본적인 DP 문제!
기존에는 i-2에서 1가지였다면, 2가지로 늘었다는게 차이점.
DP[N] = DP[N-1] + DP[N-2]*2
*/