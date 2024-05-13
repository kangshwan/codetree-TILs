#include <iostream>
#include <list>
#include <string>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    string s;
    cin >> s;
    list<char> l;
    for(int i = 0 ; i < n ; i++){
        l.push_back(s[i]);
    }
    list<char>::iterator it;
    it = l.end();
    char command;
    for(int i = 0 ; i < m ; i++){
        cin >> command;
        if (command == 'L'){
            it--;
        }
        else if (command == 'R'){
            it++;
        }
        else if (command == 'D'){
            it = l.erase(it);
        }
        else if (command == 'P'){
            char c;
            cin >> c;
            l.insert(it, c);
        }
    }
    for(it = l.begin() ; it != l.end();it++){
        cout << *it;
    }
    return 0;
}