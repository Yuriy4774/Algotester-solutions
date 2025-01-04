#include <iostream>
#include <algorithm> 

using namespace std;

int main(){
    int a,b,c,d;

    cin >> a >> b >> c >> d;
    int d1,d2;
    d1 = (a+c-1) / c;
    d2 = (b+d-1) / d;
    cout << max(d1,d2) << endl;
}
