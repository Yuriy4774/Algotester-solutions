#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    char left,rigth;
    string res;
    cin >> n;

    vector<char> sp(n);
    for (int i = 0; i < n; ++i) cin >> sp[i];
    
    if (sp[0] == '*'){
        res+='*';
    }
    else if (sp[1] == '*'){
        res+='1';
    }
    else{
        res+='0';
    }
    
    for (int i = 1; i < n-1; i++)
    {
        left = sp[i-1],rigth = sp[i+1];
        if (sp[i] == '*'){
            res+= '*';
        }
        else if (left == '*' && rigth == '*'){
            res += '2';
        }
        else if (left == '*' || rigth == '*')
        {
            res += '1';
        }
        else{
            res+= '0';
        }
    }

    if (sp[n-1] == '*'){
        res+='*';
    }
    else if (sp[n-2] == '*'){
        res+='1';
    }
    else{
        res+='0';
    }
    cout << res << endl;

    return 0;
}
