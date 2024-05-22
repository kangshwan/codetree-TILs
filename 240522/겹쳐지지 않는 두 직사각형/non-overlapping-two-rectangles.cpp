#include <iostream>

int N, M;
bool visited1[5][5];
bool visited2[5][5];
int board[5][5];
int ans = -25000;

using namespace std;

void simulate(){
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < M ; j++){
            // 첫번째 사각형의 좌상단 꼭짓점 좌표, (i, j)
            // 얼마나 큰 크기의 사각형을 선택할 지 결정해야한다.
            for(int row1 = 1 ; row1 <= N ; row1++){
                for(int col1 = 1 ; col1 <= M ; col1++){
                    // 현재 좌표에서 row1, col1 만큼의 크기를 잡았을 때 범위를 벗어나는지 확인
                    if(i+row1 > N or j+col1 > M) continue; //범위를 벗어났으므로 다시 row1, col1 선정
                    int sum1 = 0;
                    // row1, col1이 선정 완료되었으므로, visited처리한다.
                    for(int x_idx = i ; x_idx < i+row1 ; x_idx++){
                        for(int y_idx = j ; y_idx < j+col1 ; y_idx++){
                            sum1 += board[x_idx][y_idx];
                            visited1[x_idx][y_idx] = true;
                        }
                    }

                    
                    // 첫번째 사각형을 안전하게 구현을 완료했으므로, 남은 영역에서 가능한 두번째 사각형의 좌상단 꼭짓점 좌표를 선택한다.
                    // 선택한 이후, 동일한 과정을 거쳐 사각형을 구현해준다!

                    for(int k = 0 ; k < N ; k++){
                        for(int l = 0 ; l < M ; l++){
                            // 두번째 사각형의 좌상단 꼭짓점 좌표 (k, l)
                            // 얼마나 큰 크기의 사각형을 선택할 지 결정해야한다.
                            // (k, l은 visited된 좌표이면 안된다.)
                            if(visited1[k][l]) continue;
                            for(int row2 = 1 ; row2 <= N ; row2++){
                                int flag = false;
                                for(int col2 = 1 ; col2 <= M ; col2++){
                                    //현재 좌표(k, l)에서 row2, col2만큼의 크기를 잡았을 때 범위를 벗어나는지 확인
                                    if(k+row2 > N or l+col2 > M) continue;
                                    int sum2 = 0;
                                    for(int x_idx = k ; x_idx < k+row2 ; x_idx++){
                                        for(int y_idx = l ; y_idx < l+col2 ; y_idx++){
                                            if(visited1[x_idx][y_idx]){
                                                flag = true;
                                                break;
                                            }
                                            sum2 += board[x_idx][y_idx];
                                            visited2[x_idx][y_idx] = true;
                                        }
                                        if(flag){
                                            for(int x_idx = k ; x_idx < k+row2 ; x_idx++){
                                                for(int y_idx = l ; y_idx < l+col2 ; y_idx++){
                                                    visited2[x_idx][y_idx] = false;
                                                }
                                            }
                                            flag=false;
                                            continue;
                                        }
                                    }
                                    
                                    ans = max(sum1+sum2, ans);
                                    for(int x_idx = k ; x_idx < k+row2 ; x_idx++){
                                        for(int y_idx = l ; y_idx < l+col2 ; y_idx++){
                                            visited2[x_idx][y_idx] = false;
                                        }
                                    }
                                }
                            }
                        }
                    }

                    //visited 초기화
                    for(int x_idx = i ; x_idx < i+row1 ; x_idx++){
                        for(int y_idx = j ; y_idx < j+col1 ; y_idx++){
                            visited1[x_idx][y_idx] = false;
                        }
                    }
                }
            }
        }
    }
}
int main() {
    cin >> N >> M;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> board[i][j];
        }
    }
    simulate();
    cout << ans;
    return 0;
}

/*
NxM영역.
겹치지않는 두 직사각형을 적절하게 잡아야 한다.

x,y에서 잡을 수 있는 모든 경우의 수를 구한 뒤, True로 visited 표기한다.
이후, 남은 영역에 대해서 잡을 수 있는 모든 경우의 수를 구하여 sum을 구한다.
각 각 가능한 직사각형 개수는 가로 5, 세로 5의 모든 경우의 수로 결정한다.

1. 첫번째 사각형을 잡는다.
2. 첫번째 사각형을 피해 두번째 사각형을 잡는다.
3. 합을 구한다.
happy. 되겠냐?
*/