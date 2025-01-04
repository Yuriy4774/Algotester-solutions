#include <iostream>

int main(){
    int n,s;
    std::cin >> n >> s;
    int sp[n];
    int n_sp[n];
    for (int i = 0; i < n; i++)
    {
        std::cin >> sp[i];
    }
    for (int i = 0; i < n; i++)
    {
        std::cin >> n_sp[i];
    }
    
    
    for (int i = 0; i < n ; i++)
    {
        s = s - (std::abs(sp[i] - n_sp[i]));
    }
    std::cout << s;
    

}