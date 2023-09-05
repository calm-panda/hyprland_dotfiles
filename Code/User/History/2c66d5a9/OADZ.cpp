#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin>>n>>m;
    
    unordered_set<string> st1, st2;
    // U, R, D, L
    int *dx = new int[4]{0, 1, 0, -1};
    int *dy = new int[4]{-1, 0, 1, 0};

    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < m; j++) {
            int tmp; cin>>tmp;

            bool inOne = false, inTwo = false;
            if (tmp == 1) {
                for (size_t k = 0; k < 4; k++) {
                    inOne |= (st1.find(to_string(i+dx[k])+" "+to_string(j+dy[k])) != st1.end());
                    inTwo |= (st2.find(to_string(i+dx[k])+" "+to_string(j+dy[k])) != st2.end());
                }
                string key = to_string(i)+" "+to_string(j);
                if (inOne) {
                    st1.insert(key);
                } else if (inTwo) {
                    st2.insert(key);
                } else {
                    st1.insert(key);
                }
            }
        }
    }
    
    return 0;
}