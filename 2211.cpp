#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> sp(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if ((i+j) % 2 == 0){
                sp[i][j] = 1;
            }
            else{
                sp[i][j] = 0;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << sp[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}

