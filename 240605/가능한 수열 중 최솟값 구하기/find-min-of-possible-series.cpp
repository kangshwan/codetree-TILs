#include <iostream>
#include <vector>
using namespace std;
vector<int> answer;
vector<int> sequence;
int N;
bool done = false;

bool seqChecker(){
    int checkSize = 5;
    if(sequence.size()==checkSize && sequence[4] == 4) return true;
    return false;
}

bool Movable(){
    // 비어있는 경우
    if(sequence.size() == 1) return true;
    int left_start = sequence.size()-2, right_start = sequence.size()-1;
    //45464
    //01234
    //left_start = 3, right_start = 4
    for(int checker = 1 ; checker <= sequence.size()/2 ; checker++){
        // now checker = 2
        //left_start = 2, right_start = 4
        left_start = sequence.size()-checker-1, right_start = sequence.size()-1;
        int left = left_start, right = right_start;
        bool same = true;
        for(int i = 0 ; i < checker ; i++){
            // if(seqChecker()) cout << left << ' ' << right <<'\n';
            if(sequence[left] != sequence[right]){
                same = false;
                break;
            }
            left--;
            right--;
        }
        if(same) {
            // if(seqChecker()) cout << "FUCKYOU\n";
            return false;
        }
    return true;
}
void Choose(int cnt){
    if(cnt == N){
        for(auto k:sequence){
            cout << k;
        }
        done=true;
        return;
    }
    for(int i = 4 ; i <= 6 ; i++){
        // 여기서 sequence에 대한 checking이 들어가야 할 것 같다.
        // sequence의 길이가 홀수인 경우에는 "절 대" 중복될 수 없다.
        // 입력 자체에서 중복되며 들어가는 것을 방지할 것이기 때문에, 444나 54665와 같은 일은 발생하지 않도록 작성할 것이다.
        // 그럼 길이가 짝수일때만 확인하게 되는데, , , 짝수일 때는 절반부터 확인해 나가는 코드를 작성하자.
        // 45645
        // 01234

        // 0부터, 3부터 체크 --> 0, 5/2 + 1
        sequence.push_back(i);
        if(Movable()){
            Choose(cnt+1);
        }
        if(done) return;
        sequence.pop_back();
    }
}
int main() {
    cin >> N;
    Choose(0);
    return 0;
}