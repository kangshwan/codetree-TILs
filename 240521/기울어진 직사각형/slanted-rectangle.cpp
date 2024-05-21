#include <iostream>

using namespace std;

int N;
int board[20][20];

int dx[4] = {-1,-1,1,1};
int dy[4] = {1,-1,-1,1};

int ans = -1;

bool inRange(int x, int y){
    return 0 <= x and x < N and 0 <= y and y < N;
}

void move(int row, int col, int cnt, int sum, int one = 0, int two = 0){
    if(cnt == 0){
        int possible = min(N-col-1, row);
        int n_sum = 0;
        int n_row = row;
        int n_col = col;
        for(int i = 1 ; i <= possible ; i++){
            for(int rpt = 0 ; rpt < i ; rpt++){
                n_row = n_row + dx[cnt];
                n_col = n_col + dy[cnt];
                if(!inRange(n_row, n_col)) return; // 아마...안걸릴듯. 그래도 혹시 모르니~
                n_sum += board[n_row][n_col];
            }
            move(n_row, n_col, cnt+1, n_sum, i);
            n_row = row;
            n_col = col;
            n_sum = 0;
        }
    }
    else if(cnt == 1){
        int possible = min(row, col);
        if(possible == 0) return; // 이걸로 아마.. inRange를 모두 잘랐을 것 같지만 혹시 모르니 커트해둔다.
        int n_sum = sum;
        int n_row = row;
        int n_col = col;
        for(int i = 1 ; i <= possible ; i++){
            for(int rpt = 0 ; rpt < i ; rpt++){
                n_row = n_row + dx[cnt];
                n_col = n_col + dy[cnt];
                if(!inRange(n_row, n_col)) return; // 아마...안걸릴듯. 그래도 혹시 모르니~
                n_sum += board[n_row][n_col];
            }
            move(n_row, n_col, cnt+1, n_sum, one, i);
            n_row = row;
            n_col = col;
            n_sum = sum;
        }
    }
    else{
        // do action 3
        int n_row = row;
        int n_col = col;
        int n_sum = sum;
        for(int i = 0 ; i < one ; i++){
            n_row += dx[2];
            n_col += dy[2];
            if(!inRange(n_row, n_col)) return; //이건 돌 것이다!
            n_sum += board[n_row][n_col];
        }

        // do action 4
        for(int i = 0 ; i < two ; i++){
            n_row += dx[3];
            n_col += dy[3];
            // if(!inRange(n_row, n_col)) return; //할 필요 없다
            n_sum += board[n_row][n_col];
        }
        ans = max(ans, n_sum);
    }
    return;
}

int main() {
    // board 입력 받기
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> board[i][j];
        }
    }

    // row == 3부터 가능한 모든 경우의 수 순회하기.
    for(int row = 2 ; row < N ; row++){
        for(int col = 1 ; col < N-1 ; col++){
            move(row, col, 0, 0);
        }
    }
    cout << ans;
    return 0;
}

/*
NxN 격자 정보 주어짐. (1 이상 100 이하)
가능한 기울어진 직사각형중 합이 최대로 되는 경우 탐색
3번째 줄 부터 가능한 범위를 모두 탐색하며 가능한 모든 경우의 수를 탐색한다(브루트포스)
각 방향으로 이동할 수 있는 횟수는 1과 3이 같고, 2와 4가 같다.
그러므로 1,2에 대해서 가능한 모든 가지수를 탐색하면 된다.
최대가 20x20이고, 올라갈 수 있는 횟수는 현재 row에 따라서 결정된다.
ex) row==20, col=1에서 부터 시작한다면 1이 가능한 횟수는 1번부터 20-2번 가능하다. 총 1~18번까지 가능.
2번이 가능한 경우의 수는 1번이 몇번 진행하느냐에 따라서 결정된다.
1번이 18번 이동했다면, 2번은 1번만 이동이 가능하다.

규칙을 20x20에서 세우기 어려우니, 5x5에서 세워보자.
이동1이 가능한 경우의 수: 5-col+1, 이동 1이 가능한 경우의 수는 N-col+1이다.
col=0일때 4
col=1일때 3
col=2일때 2
col=3일때 1
col=4일때 0
N=5,
가능한 경우의 수 : N-col-1
하지만 항상 마지막 줄에서 시작하지는 않으니, row에 대한 수식도 결정한 뒤, col과 row로 결정되는것 중 작은것이 가능한 경우의 수다.
row의 경우, row이 가능한 경우의 수다.
모든 이동이 가능한 경우의 수는 현재 위치에서 min(N-col-1, row)이다!

이동 2의 경우에는, 현재 좌표의 min값 자체가 좌상단으로 올라갈 수 있는 경우다!
따라서 이동 2를 진행할 때에는 min(row,col)을 구한 뒤 재귀 돌리자.
시간제한이 1초.
bruteforce로 가능한 경우의 수인가?
일단..대충 20x20을 모두 순회한다고 가정하고..1
최대 가능한 가지수가 18가지, 그냥 행동 1,2 둘 다 18번 한다고 치면
20x20x18x18x2
259,200번! 너무 귀여운 숫자고
*/