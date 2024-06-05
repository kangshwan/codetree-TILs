#include <iostream>
#include <vector>
#include <tuple>
using namespace std;
int answer = 0;
int N;
vector<vector<int>> board(4, vector<int>(4));
vector<vector<int>> direction(4, vector<int>(4));

int dx[9] = {0,-1,-1,0,1,1,1,0,-1};
int dy[9] = {0,0,1,1,1,0,-1,-1,-1};

bool InRange(int x, int y){
    return 0 <= x and x < N and 0 <= y and y < N;
}
void Choose(int x, int y, int cnt){
    //check movable coordinate
    vector<tuple<int, int>> movable;
    int cur_dir = direction[x][y];
    int nx = x + dx[cur_dir], ny = y + dy[cur_dir];
    while(InRange(nx, ny)){
        if(board[nx][ny] > board[x][y]){
            movable.push_back({nx, ny});
        }
        nx = nx + dx[cur_dir], ny = ny + dy[cur_dir];
    }
    if(movable.empty()){
        answer = max(answer, cnt);
        return;
    }
    for(auto k: movable){
        Choose(get<0>(k), get<1>(k), cnt+1);
    }
}
int main() {
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> board[i][j];
        }
    }
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> direction[i][j];
        }
    }
    int r, c;
    cin >> r >> c;
    Choose(r-1, c-1, 0);
    cout << answer;
    return 0;
}
/*
1. 먼저 이동 방향 및 이동 가능한 좌표를 확인. -> 이때, 함수 내부에서 이동 가능한 좌표를 저장할 vector를 생성하여 함수 안에서만 살아있도록 한다!
2. 이동 가능한 좌표들에 대해서 이동.

N=4이므로, ~~16가지를 16번 모두 이동가능한 경우, . . 16^16이 되지만, 숫자보다 커야한다는 조건이 있기 때문에 실제로는 그보다 더 작을 것이다.~~
는 아니고, 시작 위치가 주어지기 때문에 최대 3칸 이동할 수 있고, 모든 가는 위치들이 현재 위치보다 크다고 가정하면 최대 8번 이동 가능하다.
따라서 약 3^8정도 걸린다!(6561)
아마도 O(3^8)정도로 마무리 될 수 있을것 같다..
*/