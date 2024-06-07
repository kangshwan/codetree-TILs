#include <iostream>
#include <queue>
#include <vector>
#define MAX_N 100

using namespace std;

int N, H, M;
int board[MAX_N][MAX_N];
int answer[MAX_N][MAX_N];
int visited[MAX_N][MAX_N];
int dx[4] = {0,1,0,-1};
int dy[4] = {-1,0,1,0};
vector<pair<int, int>> human_loc;

void Clean(){
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            visited[i][j] = 0;
        }
    }
}

bool InRange(int x, int y){
    return 0 <= x && x < N && 0 <= y && y < N;
}


void BFS(int start_x, int start_y){
    queue<pair<int, int>> Q;
    Clean();
    Q.push({start_x, start_y});
    visited[start_x][start_y] = 1;
    while(!Q.empty()){
        int x = Q.front().first, y = Q.front().second;
        Q.pop();
        for(int dir = 0 ; dir < 4 ; dir++){
            int nx = x + dx[dir], ny = y + dy[dir];
            if(InRange(nx, ny) && board[nx][ny] != 1 && !visited[nx][ny]){
                if(board[nx][ny] == 3){
                    answer[start_x][start_y] = visited[x][y];
                    return;
                }
                visited[nx][ny] = visited[x][y] + 1;
                Q.push({nx, ny});
            }
        }
    }
    answer[start_x][start_y] = -1;
}

int main() {
    cin >> N >> H >> M;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> board[i][j];
        }
    }
    // N*N 격자 순회하며, 2인 순간부터 BFS 수행. BFS 수행 이후에 visited를 새로 초기화 하는것을 잊지 말자.
    for(int x = 0 ; x < N ; x++){
        for(int y = 0 ; y < N ; y++){
            if(board[x][y] == 2){
                BFS(x, y);
            }
        }
    }
    // 정답 출력
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << answer[i][j] << ' ';
        }cout << '\n';
    }
    return 0;
}
/*
plan:
2, 즉 사람의 위치를 모두 뽑은 이후, 각 사람에 대해서 3까지 bfs를 진행한다.
3에 도착했다면 해당 숫자를 answer 배열에 적는다.
도착하지 못했다면 -1을 asnwer 배열에 적는다.
*/