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

    // DP 초기화
    DP[0][0] = board[0][0];
    for(int i = 1 ; i < N ; i++){
        DP[0][i] = min(DP[0][i-1], board[0][i]);
        DP[i][0] = min(DP[i-1][0], board[i][0]);
    }
    for(int i = 1 ; i < N ; i++){
        for(int j = 1 ; j < N ; j++){
            DP[i][j] = min(max(DP[i-1][j], DP[i][j-1]), board[i][j]);
        }
    }
    cout << DP[N-1][N-1];
    return 0;
}

/*
이전 문제를 살짝 꼬은 문제.
지나온 숫자중 최소값을 최대로하는것.
DP에 저장될 것은 최대인 최소값.
DP[i][j]까지 어떤 경로로 왔던지간에, [i][j]에서 최대인 최소값이라는 뜻.
DP[i][j] = DP[i-1][j], DP[i][j-1], board[i][j]

흠...
예제 1로 한번 테스트 해보자.
DP
5 2 2
3 0 0
1 0 0
초기값.
이후 진행.
DP[1][1] = DP[0][1] == 2, DP[1][0] == 3, board[1][1] == 2
DP[1][1]에서는 반드시 board[1][1]을 거친다. 최소는 2..
DP[0][1] DP[1][0]에서는 큰것을 가져오고, board[1][1]과 비교에서 작은것을 선택하면 된다.
DP[i][j] = min(max(DP[i-1][j], DP[i][j-1]), board[i][j])
5 2 2
3 2 1
1 2 2
======
3
4 3 2
3 4 5
4 2 8

DP
4 3 2
3 0 0
3 0 0

4 3 2
3 3 3
3 2 3
*/