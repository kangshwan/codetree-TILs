#include <iostream>
#include <vector>
using namespace std;
vector<int> piece = {0,0,0,0,0,0,0,0,0,0,0,0};
vector<int> step_size;
vector<int> move_piece;
// step_size.size() == move_piece.size()
int answer = 0;
int N, M, K;

void Move(){
    for(int i = 0 ; i < N ; i++){
        int idx = move_piece[i];
        piece[idx] += step_size[i];
    }
    // 끝까지 도달한 말 확인
    int cnt = 0;
    for(int i = 0 ; i < K ; i++){
        if(piece[i] >= M-1) cnt++;
        piece[i] = 0;
    }
    answer = max(answer, cnt);
}

void Choose(int idx){
    if(idx == N){
        Move();
        return;
    }
    for(int i = 0 ; i < K ; i++){
        move_piece.push_back(i);
        Choose(idx+1);
        move_piece.pop_back();
    }
    return;
}
int main() {
    cin >> N >> M >> K;
    int tmp;
    for(int i = 0 ; i < N ; i++){
        cin >> tmp;
        step_size.push_back(tmp);
    }
    Choose(0);
    cout << answer;
    return 0;
}