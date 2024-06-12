#include <iostream>
#define MAX_N 100

using namespace std;

int N;
pair<int, int> DP[MAX_N][MAX_N];
int board[MAX_N][MAX_N];

int absolute(pair<int, int> num){
    return abs(num.second - num.first);
}

int main() {
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> board[i][j];
            // initialize DPh, DPl
        }
    }
    // initialize DP
    // row에 대해서 초기화
    DP[0][0] = {board[0][0], board[0][0]};
    for(int i = 1 ; i < N ; i++){
        int low = DP[0][i-1].first, high = DP[0][i-1].second;
        if(board[0][i] < low){
            DP[0][i] = {board[0][i], high};
        }
        else if(board[0][i] > high){
            DP[0][i] = {low, board[0][i]};
        }
        else{
            DP[0][i] = DP[0][i-1];
        }

        if(board[i][0] < low){
            DP[i][0] = {board[i][0], high};
        }
        else if(board[i][0] > high){
            DP[i][0] = {low, board[i][0]};
        }
        else{
            DP[i][0] = DP[i-1][0];
        }
    }
    for(int i = 1 ; i < N ; i++){
        for(int j = 1 ; j < N ; j++){
            // board[i][j]가 들어갔을 때, 위쪽에서 받아오는 것과 아래쪽에서 받아오는 것 중 절대값이 더 작은것으로 선택한다.
            pair<int, int> upper = DP[i-1][j], lower = DP[i][j-1];

            // update upper and lower when board[i][j] is in.
            if(board[i][j] < upper.first){
                upper = {board[i][j], upper.second};
            }
            else if(board[i][j] > upper.second){
                upper = {upper.first, board[i][j]};
            }
            
            if(board[i][j] < lower.first){
                lower = {board[i][j], lower.second};
            }
            else if(board[i][j] > lower.second){
                lower = {lower.first, board[i][j]};
            }
            int upper_abs = absolute(upper), lower_abs = absolute(lower);
            if(upper_abs < lower_abs){
                DP[i][j] = upper;
            }else{
                DP[i][j] = lower;
            }
        }
    }
    // cout << abs(DPh[N-1][N-1] - DPl[N-1][N-1]);
    // for(int i = 0 ; i < N ; i++){
    //     for(int j = 0 ; j < N ; j++){
    //         cout << '{' << DP[i][j].first << ", " << DP[i][j].second << "} ";
    //     }cout << '\n';
    // }
    cout << absolute(DP[N-1][N-1]);
    return 0;
}

/*
DP테이블이 가지고 있어야할 것은 무엇일까??
우선, 최소를 가지고 있는 DP테이블
3
1 2 3
5 4 6
7 1 2

DP
1 1 1
1 101 101
1 101 101

[1,1]에서 최소를 업데이트할 때, DP[0,1], DP[1,0]중 큰 값과 본인의 크기를 비교한다.

DP
1 1 1
1 1 101
1 101 101

아마도 최소 DP의 경우 모두 1로 범벅될 것이다.
DP
1 1 1
1 1 1
1 1 1

최대 DP도 동일하게 구하나, 절대값이 최소가 되어야 하기 때문에 근처 DP중 값이 작은 것을 가져와야 한다.

DP
1 2 3
5 0 0
7 0 0

[1,1]을 업데이트 할 때, DP[0,1], DP[1,0]중 작은값 2, 그리고 본인 4 중 큰것 -> 4

DP
1 2 3
5 4 6
7 4 4

결국 4-1 = 3! 이라는 좋은 결론을 얻을 수 있다.

최대와 최소의 경로가 다르다...!
어쩔수 없이 한 DP에 두가지 값을 가지고 있게 해야한다.

4
20 30 51 30
22 10 12 1
10 25 35 21
34 36 20 20

DPl
20 20 20 20
20 10 12 1
10 10 
10
*/