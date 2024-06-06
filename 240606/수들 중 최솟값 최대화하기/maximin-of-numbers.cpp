#include <iostream>
#include <vector>
#define MAX_N 10
using namespace std;

int N;
int board[MAX_N][MAX_N];
int visited[MAX_N];
vector<int> permutation;

int answer = 0;

void Choose(int cnt){
    if(cnt == N){
        int min_val = 10001;
        for(int i = 0 ; i < N ; i++){
            min_val = min(min_val, board[i][permutation[i]]);
        }
        answer = max(answer, min_val);
        return;
    }
    for(int i = 0 ; i < N ; i++){
        if(!visited[i]){
            visited[i] = true;
            permutation.push_back(i);
            Choose(cnt+1);
            permutation.pop_back();
            visited[i] = false;
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