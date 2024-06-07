#include <iostream>
#include <queue>
#include <tuple>
#define MAX_N 100
#define MAX_K 8

using namespace std;

int N, K;
int visited[MAX_K+1][MAX_N][MAX_N];
int board[MAX_N][MAX_N];
int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0};
int r1, c1, r2, c2;
queue<tuple<int, int, int>> Q;

bool InRange(int x, int y){
    return 0 <= x and x < N and 0 <= y and y < N;
}

void BFS(int x, int y){
    Q.push({0,x,y});
    visited[0][x][y] = 1;
    while(!Q.empty()){
        tuple<int, int, int> data = Q.front();
        int k = get<0>(data), x = get<1>(data), y = get<2>(data);
        Q.pop();
        for(int dir = 0 ; dir < 4 ; dir++){
            int nx = x + dx[dir], ny = y + dy[dir];
            if(InRange(nx, ny) and !visited[k][nx][ny]){
                //nx, ny가 벽인지 확인
                if(board[nx][ny] == 1){
                    // 벽이라면, k가 남아있는지 확인
                    if(k < K){
                        //남아있다면
                        //nx, ny가 도착지점인지 확인
                        if(nx == r2 and ny == c2){
                            cout << visited[k][x][y];
                            return;
                        }
                        visited[k+1][nx][ny] = visited[k][x][y] + 1;
                        Q.push({k+1,nx,ny});
                    }
                }
                //벽이 아니라면
                else{
                    //nx, ny가 도착지점인지 확인
                    if(nx == r2 and ny == c2){
                        cout << visited[k][x][y];
                        return;
                    }
                    visited[k][nx][ny] = visited[k][x][y] + 1;
                    Q.push({k,nx,ny});
                }
            }
        }
    }
    cout << -1;
    return;
}

int main() {
    cin >> N >> K;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> board[i][j];
        }
    }
    cin >> r1 >> c1 >> r2 >> c2;
    r1--;c1--;r2--;c2--;
    BFS(r1,c1);
    return 0;
}