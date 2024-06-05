#include <iostream>
#include <vector>
using namespace std;
int K, N;
vector<int> answer;
bool Addable(int idx, int target){
    if(idx < 2) return true;
    int dup_cnt = 0;
    for(int i = idx-1 ; i > idx-3 ; i--){
        if(answer[i] == target) dup_cnt++;
    }
    if(dup_cnt == 2) return false;
    return true;

}
void Choose(int cnt){
    if(cnt == N){
        for(int i = 0 ; i < answer.size() ; i++){
            cout << answer[i] << ' ';
        }
        cout << '\n';
        return;
    }
    for(int i = 1 ; i <= K ; i++){
        if(Addable(cnt, i)){
            answer.push_back(i);
            Choose(cnt+1);
            answer.pop_back();
        }
    }
    return;
}
int main() {
    
    cin >> K >> N;
    Choose(0);
    return 0;
}