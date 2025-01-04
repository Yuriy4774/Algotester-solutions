#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

int main() {
    int n,w_v = 0,w_k = 0,r_v = 0,r_k = 0;
    string rach;

    cin >> n;
    cin >> rach;
    for (int i = 0; i < rach.size(); i++)
    {
        if (rach[i] == 'V'){
            r_v += 1;
        }
        else if (rach[i] == 'K'){
            r_k += 1;
        }

        if ((r_k >= 11 || r_v >= 11) && abs(r_k - r_v) >= 2){
            if (r_k > r_v){
                w_k += 1;
            }
            if (r_v > r_k){
                w_v += 1;
            }
            r_k = 0;
            r_v = 0;
        }
    }
    cout << w_k << ":" << w_v << endl;
    if (r_k > 0 || r_v > 0){
        cout << r_k << ":" << r_v << endl;
    }
    
}