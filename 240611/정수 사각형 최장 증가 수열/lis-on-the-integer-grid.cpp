#include <iostream>
#include <map>
#include <vector>
#define MAX_N 500

using namespace std;

int N;
int DP[MAX_N][MAX_N];
int board[MAX_N][MAX_N];
map<int, vector<pair<int, int>>> hashmap;
int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0};

bool InRange(int x, int y){
    return 0 <= x and x < N and 0 <= y and y < N;
}
int main() {
    cin >> N;
    // 이론상 500*500번, N^2
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> board[i][j];
            hashmap[board[i][j]].push_back({i,j});
            DP[i][j] = 1;
        }
    }
    // 이론상 500*500*4, 4*N^2
    for(auto& val: hashmap){
        for(pair<int, int> loc: val.second){
            int x = loc.first, y = loc.second;
            // DP의 상, 하, 좌, 우 체크하여 작은게 있다면 작은것들 중 max를 찾아 더하기.
            int max_val = 0;
            for(int dir = 0 ; dir < 4 ; dir++){
                int nx = x + dx[dir], ny = y + dy[dir];
                if(InRange(nx, ny) and board[nx][ny] < board[x][y]){
                    max_val = max(max_val, DP[nx][ny]);
                }
            }
            DP[x][y] += max_val;
        }
    }
    // N^2
    int answer = 1;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            answer = max(answer, DP[i][j]);
        }
    }
    cout << answer;
    return 0;
}

/*
우선적으로 모든 좌표 i,j는 1칸씩 움직일 수 있다.
3
2 2 1
3 1 2
4 1 2

DP
1 1 1
1 1 1
1 1 1

DP[0][0] = 1
DP[0][1] = 상하좌우 체크해서 board[0][1]보다 작은7게 있는지 확인하고, 작은게 있다면 작은것들 중 최대값으로 업데이트.
즉 [0][0], [0][2], [1][1] 중 board[0][1]보다 작은 [0][2], [1][1]이 있고, DP[0][2]와 DP[1][1]은 서로 1이기 때문에, 큰 값을 더한다.
DP
1 2 1
1 1 1
1 1 1
DP[1][0]은, 위와 동일하게 다음처럼 업데이트
DP
1 2 1
2 1 1
1 1 1

DP
1 2 1
2 1 2
1 1 1
DP[2][0]도 다음처럼 업데이트
DP
1 2 1
2 1 2
3 1 1

DP
1 2 1
2 1 2
3 1 2

중에서 최대는 3.

예제 2로 증명해보자.

3
5 1 3
6 1 4
7 2 3

DP
2 1 2
3 1 3
4 2 3
흠...
작은 수들부터 DP를 업데이트 한다면?

DP
1 1 1
1 1 1
1 1 1
// 1

DP
1 1 1
1 1 1
1 2 1
// 2

DP
1 1 2
1 1 1
1 2 3
// 3

DP
1 1 2
1 1 4
1 2 3
// 4

DP
2 1 2
1 1 4
1 2 3
// 5

DP
2 1 2
3 1 4
1 2 3
//6

DP
2 1 2
3 1 4
4 2 3

MAX_val = 4.

시간복잡도는 충분할까?
숫자가 총 500개니, 500개를 저장할 key-value가 있으면 좋겠고, 이를 오름차순으로 정렬하면 더욱 좋겠다.
500개의 숫자가 모두 다르다고 생각하면, 정렬하는데에 hashmap을 사용하자.

hashmap을 사용해서 정렬한 이후, hashmap에 맞는 순서대로 순회를 진행한다.
최악의 경우 500*500*500번 진행되고, 1억 2천... 끄응 1초를 넘어선다.
순회하지 않고 hashmap에 좌표를 저장하고 있다면 500*500번만 진행하면 된다!
될지는 모르겠지만 일단 let's go.
*/