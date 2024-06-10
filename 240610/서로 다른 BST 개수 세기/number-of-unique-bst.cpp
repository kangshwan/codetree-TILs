#include <iostream>
#define MAX_N 19

using namespace std;

int N;
int DP[MAX_N+1] = {1, 1, 2, 5};
int main() {
    cin >> N;
    for(int i = 4 ; i <= N ; i++){
        int tmp = 0;
        for(int j = 0 ; j <= i ; j++){
            tmp += DP[i-j] * DP[j-1];
        }
        DP[i] = tmp;
    }
    cout << DP[N];
    return 0;
}

/*
뭔가 leaf 개수를 저장하고 있는 게 필요해보인다.

*/