#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    int res = 0;
    vector<int> kup = {500, 200, 100, 50, 20, 10, 5, 2, 1};//можна додати 1000 якщо треба
    
    cin >> n;

    for (int i = 0; i < kup.size(); i++) {
        res += n / kup[i];
        n = n % kup[i];
        //cout << res << " " << n << endl;
    }

    cout << res << endl;

    return 0;
}

