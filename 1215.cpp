#include <iostream>

int main(){
    int n;
    std::cin >> n;

    bool winning[n];
    winning[0] = false;

    for (int i = 1; i <= n; i++)
    {
        winning[i] = false;
        if (winning[i-1] == false)
        {
            winning[i] = true;
        }
        if (i >= 4 and winning[i-4] == false)
        {
            winning[i] = true;
        }
        if (i >= 7 and winning[i-7] == false)
        {
            winning[i] = true;
        }
    }
    if (winning[n] == 0)
    {
        std::cout << "Zenyk";
    }
    else{
        std::cout << "Marichka";
    }
    
    
}
