#include <iostream>
#include <vector>
#define MAX_N 8

using namespace std;

vector<int> permu;
bool visited[MAX_N+1];
int N;
void Permutation(int cnt){
    if(cnt == N){
        for(auto k: permu){
            cout << k << ' ';
        }cout << '\n';
        return;
    }
    for(int i = 1 ; i <= N ; i++){
        if(!visited[i]){
            visited[i] = true;
            permu.push_back(i);
            Permutation(cnt+1);
            permu.pop_back();
            visited[i] = false;
        }
    }
}

int main() {
    cin >> N;
    Permutation(0);
    return 0;
}