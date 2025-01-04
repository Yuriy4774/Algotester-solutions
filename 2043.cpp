#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    long long res;

    cin >> n;
    res = (static_cast<long long>(n) * (n+1) * (n+2)) / 2;
    cout << res << endl;

    return 0;
}
