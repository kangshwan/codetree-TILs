#include <iostream>
#include <queue>
#define MAX_N 100

using namespace std;

int N;
int visited[MAX_N][MAX_N]={};
queue<pair<int, int>> Q;
int start_x, start_y, end_x, end_y;
int dx[8] = {-2, -1, 1, 2, 2, 1, -1, -2};
int dy[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int answer = -1;

bool InRange(int x, int y){
    return 0 <= x and x < N and 0 <= y and y < N;
}

void Print(){
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << visited[i][j] << ' ';
        }cout << '\n';
    }
    cout << '\n';
}
int main() {
    cin >> N;
    cin >> start_x >> start_y >> end_x >> end_y;
    start_x--; start_y--; end_x--; end_y--;
    if(start_x == end_x and start_y == end_y){
        cout << 0;
        return 0;
    }
    Q.push({start_x, start_y});
    visited[start_x][start_y] = 1;
    while(!Q.empty()){
        int x,y;
        x = Q.front().first;
        y = Q.front().second;
        Q.pop();
        bool reach2end = false;
        for(int dir = 0 ; dir < 8 ; dir++){
            int nx = x + dx[dir], ny = y + dy[dir];
            if(nx == end_x and ny == end_y){
                reach2end = true;
                answer = visited[x][y];
                break;
            }
            if(InRange(nx, ny) and !visited[nx][ny]){
                visited[nx][ny] = visited[x][y] + 1;
                Q.push({nx, ny});
            }
        }
        if(reach2end) break;
    }
    cout << answer;
    return 0;
}