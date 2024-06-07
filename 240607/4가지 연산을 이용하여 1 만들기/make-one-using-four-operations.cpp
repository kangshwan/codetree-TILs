#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <tuple>
#define MAX_N 1000000

using namespace std;

int N;
queue<pair<int, int>> Q;
bool visited[MAX_N + 1]={};
// auto func_list = ;
vector<function<int(int)>> funcs = {[](int x){return x % 2 == 0 ? x/2 : x;}, [](int x){return x % 3 == 0 ? x/3 : x;}, [](int x){return x-1;},[](int x){return x+1;}};

bool InRange(int x){
    return 0 < x and x <= MAX_N;
}

void BFS(int x){
    Q.push({0, x});
    visited[x] = true;
    while(!Q.empty()){
        int cnt = Q.front().first, x = Q.front().second;
        Q.pop();
        for(auto& func : funcs){
            int nx = func(x);
            if(nx == 1){
                cout << cnt+1;
                return;
            }
            if(InRange(nx) and !visited[nx]){
                Q.push({cnt+1, nx});
                visited[nx] = true;
            }
        }
        // for(int func = 0 ; func < 4 ; func++){
        //     int nx;
        //     if(func == 0){
        //         if(x % 3 == 0){
        //             nx = x / 3;
        //             Q.push({cnt+1, nx});
        //         }
        //     }
        //     if(func == 1){
        //         if(x % 2 == 0){
        //             nx = x / 2;
        //             Q.push({cnt+1, nx});
        //         }
        //     }
        //     if(func == 2){
        //         nx = x + 1;
        //         Q.push({cnt+1,})
        //     }
        //     if(func == 3){

        //     }
        //     if(nx == 1){
        //         cout << cnt + 1;
        //         return;
        //     }
        // }
    }
}

int main() {
    cin >> N;
    if(N == 1){
        cout << 0;
    }
    else{
        BFS(N);
    }
    return 0;
}

/*
쉽다. 이번에는 queue에 연산 횟수를 저장하여 넘겨주면 ok!
*/