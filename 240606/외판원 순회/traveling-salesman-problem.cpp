#include <iostream>
#include <vector>
#define MAX_N 10

using namespace std;

int N;
int matrix[MAX_N][MAX_N];
bool visited[MAX_N]={};
vector<int> paths;
int answer = 100000;
void Choose(int cnt){
    if(cnt == N-1){
        // 순회 method
        int start = 0;
        int dist = 0;
        for(auto next: paths){
            if(matrix[start][next] == 0){
                return;
            }
            dist += matrix[start][next];
            start = next;
        }
        if(matrix[start][0] == 0){
            return;
        }
        dist += matrix[start][0];
        answer = min(answer, dist);
        return;
    }
    for(int i = 1 ; i < N ; i++){
        if(!visited[i]){
            visited[i] = true;
            paths.push_back(i);
            Choose(cnt+1);
            paths.pop_back();
            visited[i] = false;
        }
    }
}
int main() {
    // 여기에 코드를 작성해주세요.
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> matrix[i][j];
        }
    }
    Choose(0);
    cout << answer;
    return 0;
}
/*
N가지 경우의 수를 뽑아둔다. 단, 1 제외.
그렇다면 어떤 일련의 거쳐가는 순서가 나오게 되고,
인접행렬로 부터 순서를 얻어와 길이를 구하면 된다!
*/