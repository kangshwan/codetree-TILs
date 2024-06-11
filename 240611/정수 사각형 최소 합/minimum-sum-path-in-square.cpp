#include <iostream>
#define MAX_N 100

using namespace std;

int N;
int DP[MAX_N][MAX_N];
int board[MAX_N][MAX_N];

int main() {
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> board[i][j];
        }
    }
    // Do first row sum
    DP[0][N-1] = board[0][N-1];
    for(int i = N-2 ; i >= 0 ; i--){
        DP[0][i] = board[0][i] + DP[0][i+1];
    }
    // Do last colum sum
    for(int i = 1 ; i < N ; i++){
        DP[i][N-1] = board[i][N-1] + DP[i-1][N-1];
    }
    // i for row
    for(int i = 1 ; i < N ; i++){
        for(int j = N-2 ; j >= 0 ; j--){
            DP[i][j] = min(DP[i-1][j], DP[i][j+1]) + board[i][j];
        }
    }
    cout << DP[N-1][0];
    return 0;
}