#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n,k;
    cin >> n >> k;

    if (k > (n-1)/ 2){
        cout << -1 << endl;
        return 0;
    }
    vector<int> sp;
    for (int i = 1; i <= n; i++)
    {
        sp.push_back(i);
    }
    for (int i = 0; i < 2*k; i+=2)
    {
        int a = sp[i];
        sp[i] = sp[i+1];
        sp[i+1] = a;
    }
    
    //output
    for (int i = 0; i < n; i++)
    {
        cout << sp[i] << " ";
    }
    cout << endl;


    return 0;
}
