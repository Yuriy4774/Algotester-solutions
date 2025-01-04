#include <iostream>

using namespace std;

int main(){
    int a,b,c,x;
    cin >> a >> b >> c >> x;
    
    if (x < a){
        cout << "gold" << endl;
        exit(0);
    }
    if (x < b){
        cout << "silver" << endl;
        exit(0);
    }
    if (x < c){
        cout << "bronze" << endl;
        exit(0);
    }
    cout << "none" << endl;

    return 0;
}
