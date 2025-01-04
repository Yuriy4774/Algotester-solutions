#include <iostream>

int main(){
    int n;
    int res = 0;
    std::cin >> n;

    for (int i = 1; i <= n; i++)
    {
        res = res + (i*i);
    }
    std::cout << res;
}
