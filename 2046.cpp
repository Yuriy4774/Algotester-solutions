#include <iostream>
#include <vector>
using namespace std;

int main(){
    long n = 0,z = 0,m = 0,res = 0,mm = 0;
    cin >> n;
    vector<int> sp(n);
    
    for (int i = 0; i < n; ++i) {
        cin >> sp[i];
        z += sp[i]; 
    }
    for (int i = 0; i < n; i++)
    {
        mm+=sp[i];
        z-=sp[i];
        m = max(m, mm);
        if (z <= m){
            res = max(res,z);
        }
    }
    cout << res << endl;


    
}
