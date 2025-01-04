#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n,k;
    cin >> n >> k;
    vector<int> sp(k);
    for (int i = 0; i < k; i++)
    {
        sp[i] = 0;
    }

    int i = 0;
    while (n > 0)
    {
        sp[i] += 1;
        i+=1;
        if (i >= k){
            i = 0;
        }
        n-=1;
    }
    for (int i = 0; i < k; i++)
    {
        if (sp[i] > 3 || sp[i] < 1){
            cout << "Impossible" << endl;
            return 0;
        }
    }
    for (int i = 0; i < k; i++)
    {
        cout << sp[i] << " ";
    }
    cout << endl;
    return 0;
    
    

    
     
}
