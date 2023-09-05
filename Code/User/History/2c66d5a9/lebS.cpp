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
            for (size_t k = 0; k < 4; k++) {
                
            }
        }
    }
    
    return 0;
}