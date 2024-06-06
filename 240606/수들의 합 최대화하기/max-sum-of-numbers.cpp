#include <iostream>
#include <vector>
#define MAX_N 10
using namespace std;

int N;
int board[MAX_N][MAX_N];
bool visited_row[MAX_N];
bool visited_col[MAX_N];
vector<int> permutation;

int answer = 0;

bool CanPaint(int num){
    int x = num / N, y = num % N;
    return !visited_row[x] and !visited_col[y];
}
void Choose(int cnt){
    if(cnt == N){
        int tmp = 0;
        for(auto num: permutation){
            int x = num / N, y = num % N;
            tmp += board[x][y];
        }
        answer = max(answer, tmp);
        return;
    }
    for(int i = 0 ; i < N*N ; i++){
        if(CanPaint(i)){
            int x = i / N, y = i % N;
            visited_row[x] = true;
            visited_col[y] = true;
            permutation.push_back(i);
            Choose(cnt+1);
            permutation.pop_back();
            visited_row[x] = false;
            visited_col[y] = false;
        }
    }

}

int main() {
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> board[i][j];
        }
    }
    Choose(0);
    cout << answer;
    return 0;
}

/*
num -> index 기술을 사용하면 해결된다.
ex)
N = 3
0 1 2 3 4 5 6 7 8 
num // N -> row
num % N -> col
0,1,2 // 3 --> 0
0,1,2 % 3 --> 0,1,2

*/