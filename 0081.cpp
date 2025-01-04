#include <iostream>
#include <functional>
#include <string>

using namespace std;

int get_hash(string value){
    hash<string> hash_func;
    return hash_func(value);
}

int main(){
    int n,len,init_hash,hash_word,res = 0;
    string sp,word;

    cin >> n;
    cin >> sp;
    len = sp.size();
    init_hash = get_hash("TOILET");
    //cout << init_hash << endl;

    for (int i = 0; i <= len - 6; i++)
    {
        word = sp.substr(i,6);
        //cout << word << endl;
        hash_word = get_hash(word);
        if (init_hash == hash_word){
            res += 1;
            i+= 5;
        }

    }
    if (res >= n){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
    

    return 0;
}
