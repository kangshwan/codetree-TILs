#include <iostream>
#include <list>
#include <string>

using namespace std;

int main() {

    list<int> s;
    string command;
    int N;
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> command;
        if(command == "push_front"){
            int num;
            cin >> num;
            s.push_front(num);
        }
        else if(command == "push_back"){
            int num;
            cin >> num;
            s.push_back(num);
        }
        else if(command == "pop_front"){
            int num = s.front();
            s.pop_front();
            cout << num << '\n';
        }
        else if(command == "pop_back"){
            int num = s.back();
            s.pop_back();
            cout << num << '\n';
        }
        else if(command == "size"){
            cout << s.size() << '\n';
        }
        else if(command == "empty"){
            cout << s.empty() << '\n';
        }
        else if(command == "front"){
            cout << s.front() << '\n';
        }
        else if(command == "back"){{
            cout << s.back() << '\n';
        }}
    }
    return 0;
}