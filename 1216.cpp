#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int mex(vector<int> &sp){
    vector<bool> was(sp.size()+1,false);
    for (int x : sp) {
        if (x < was.size()) {
            was[x] = true;
        }
    }
    for (int i = 0; i < was.size(); ++i) {
        if (!was[i]) {
            return i;
        }
    }
    return was.size();
}


int main(){
    int n;
    cin >> n;
    vector<int> sp(n);
    for (int i = 0; i < n; ++i) {
        cin >> sp[i];
    }
    
    int max_sp = *max_element(sp.begin(), sp.end());
    
    vector<int> G(max_sp+1,0);
    for (int i = 0; i <= max_sp; ++i){
        vector<int> S;
        if (i >= 1){
            S.push_back(G[i-1]);
        }
        if (i >= 4){
            S.push_back(G[i-4]);
        }
        if (i >= 7){
            S.push_back(G[i-7]);
        }
        G[i] = mex(S);
    }
    int res = 0;
    for (int i = 0; i < n; i++)
    {
        res = res ^ G[sp[i]];
    }

    
    if (res != 0) {
        cout << "Marichka" << endl;
    } else {
        cout << "Zenyk" << endl;
    }
    return 0;
}
