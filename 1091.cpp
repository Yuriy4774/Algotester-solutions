#include <iostream>
using namespace std;

int main(){
    int res = 0,n;
    string sp;
    cin >> sp;
    n = sp.size();
    if (n > 1){
        if(sp[0] == '_' && sp[1] == '_'){
            sp[0] = '#';
            res++;;
        }
        if (sp[n-1] == '_' && sp[n-2] == '_'){
            sp[n-1] = '#';
            res++;
        }
    }
    for (int i = 1; i < n-1; i++)

    {
        if (sp[i-1] == '_' && sp[i+1] == '_' && sp[i] == '_')
        {
            res+=1;
            sp[i] = '#';
            //cout << i << endl;
        }
        
    }
    cout << res << endl;
    
}
