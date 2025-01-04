#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int k1,n1,p1,k2,n2,p2,res;
    cin >> k1 >> n1 >> p1;

    cin >> k2>> n2 >> p2;

    res = min(k1,n2) + min(p1,k2) + min(n1,p2);
    cout << res;
    
    return 0;
}

